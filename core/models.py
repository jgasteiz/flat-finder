from django.db import models


ORDER_BY = (('price', 'Price'), ('age', 'Age'),)
ORDERING = (('descending', 'Descending'), ('ascending', 'Ascending'),)
LISTING_STATUS = (('rent', 'Rent'), ('sale', 'Sale'),)


class Search(models.Model):
    area = models.CharField(blank=True, max_length=128)
    postcode = models.CharField(blank=True, max_length=128)
    country = models.CharField(blank=True, max_length=128)

    radius = models.FloatField(blank=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    lat_min = models.FloatField(blank=True)
    lon_min = models.FloatField(blank=True)
    lat_max = models.FloatField(blank=True)
    lon_max = models.FloatField(blank=True)

    order_by = models.CharField(blank=True, choices=ORDER_BY, max_length=16)
    ordering = models.CharField(blank=True, choices=ORDERING, max_length=16)

    listing_status = models.CharField(blank=True, choices=LISTING_STATUS, default='rent', max_length=16)

    minimum_price = models.FloatField(blank=True)
    maximum_price = models.FloatField(blank=True)

    minimum_beds = models.FloatField(blank=True)
    maximum_beds = models.FloatField(blank=True)

    furnished = models.BooleanField(default=True)


class Property(models.Model):
    listing_id = models.TextField(verbose_name='Service id for the property')
