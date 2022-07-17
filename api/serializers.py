import json
import os

import requests

from api import exceptions
from django.contrib.auth import get_user_model
from django.db.models import Q
from geolocation.models import Geolocation
from rest_framework import serializers

User = get_user_model()

IP_STACK_URL = "http://api.ipstack.com/"
ACCESS_KEY = os.environ.get('IP_STACK_ACCESS_KEY')


class GeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geolocation
        fields = '__all__'
        extra_kwargs = {
            'url': {'allow_blank': True},
        }
        read_only_fields = (
            'continent_code', 'continent_name', 'country_code', 'country_name', 'region_code',
            'region_name', 'city', 'postcode', 'latitude', 'longitude',)

    def validate(self, attrs):
        url = attrs.get('url') or ''
        ip = attrs.get('ip_address') or ''
        if url == '' and ip == '':
            raise serializers.ValidationError('URL or IP is required')
        if url and ip:
            raise serializers.ValidationError('Please provide URL or IP')
        return attrs

    def create(self, validated_data):
        ip = validated_data.get('ip_address')
        url = validated_data.get('url')
        try:
            geolocation = Geolocation.objects.get(Q(ip_address=ip) | Q(url=url))
        except Geolocation.DoesNotExist:
            url_to_check =  url.split('//')[-1]
            param_to_check = ip or url_to_check
            url = f"{IP_STACK_URL}{param_to_check}?access_key={ACCESS_KEY}"
            try:
                response = requests.get(url)
            except:
                raise exceptions.ThirdPartyError()
            data = json.loads(response.content)
            if response.status_code != 200:
                raise Exception('something went wrong')
            if 'error' in data:
                error_code = data['error']['code']
                message = data['error']['info']
                raise serializers.ValidationError(code=error_code, detail=message)
            else:
                validated_data['ip_address'] = data['ip']
                validated_data['continent_code'] = data['continent_code']
                validated_data['continent_name'] = data['continent_name']
                validated_data['country_code'] = data['country_code']
                validated_data['country_name'] = data['country_name']
                validated_data['region_code'] = data['region_code']
                validated_data['region_name'] = data['region_name']
                validated_data['city'] = data['city']
                validated_data['postcode'] = data['zip']
                validated_data['latitude'] = data['latitude']
                validated_data['longitude'] = data['longitude']
                geolocation = super().create(validated_data)
        return geolocation


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ( "id", "username", "password", )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user
