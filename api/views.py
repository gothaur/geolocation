from api import serializers
from api.serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.db import transaction
from geolocation.models import Geolocation
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

User = get_user_model()


class GeoListView(ModelViewSet):

    queryset = Geolocation.objects.all()
    model = Geolocation
    serializer_class = serializers.GeoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'geo_id'

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()


class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
