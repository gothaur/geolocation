# Generated by Django 4.0.6 on 2022-07-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('url', models.URLField(null=True)),
                ('continent_code', models.CharField(max_length=3, null=True)),
                ('continent_name', models.CharField(max_length=32, null=True)),
                ('country_code', models.CharField(max_length=3, null=True)),
                ('country_name', models.CharField(max_length=32, null=True)),
                ('region_code', models.CharField(max_length=3, null=True)),
                ('region_name', models.CharField(max_length=32, null=True)),
                ('city', models.CharField(max_length=32, null=True)),
                ('postcode', models.CharField(max_length=32, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
            ],
        ),
    ]
