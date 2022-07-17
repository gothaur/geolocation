from django.db import models


class Geolocation(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    url = models.URLField(null=True)
    continent_code = models.CharField(max_length=3, null=True)
    continent_name = models.CharField(max_length=32, null=True)
    country_code = models.CharField(max_length=3, null=True)
    country_name = models.CharField(max_length=32, null=True)
    region_code = models.CharField(max_length=3, null=True)
    region_name = models.CharField(max_length=32, null=True)
    city = models.CharField(max_length=32, null=True)
    postcode = models.CharField(max_length=32, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return self.ip_address
