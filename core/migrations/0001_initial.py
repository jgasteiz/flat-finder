# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listing_id', models.TextField(verbose_name=b'Service id for the property')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=128, blank=True)),
                ('postcode', models.CharField(max_length=128, blank=True)),
                ('country', models.CharField(max_length=128, blank=True)),
                ('radius', models.FloatField(blank=True)),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.FloatField(blank=True)),
                ('lat_min', models.FloatField(blank=True)),
                ('lon_min', models.FloatField(blank=True)),
                ('lat_max', models.FloatField(blank=True)),
                ('lon_max', models.FloatField(blank=True)),
                ('order_by', models.CharField(blank=True, max_length=16, choices=[(b'price', b'Price'), (b'age', b'Age')])),
                ('ordering', models.CharField(blank=True, max_length=16, choices=[(b'descending', b'Descending'), (b'ascending', b'Ascending')])),
                ('listing_status', models.CharField(default=b'rent', max_length=16, blank=True, choices=[(b'rent', b'Rent'), (b'sale', b'Sale')])),
                ('minimum_price', models.FloatField(blank=True)),
                ('maximum_price', models.FloatField(blank=True)),
                ('minimum_beds', models.FloatField(blank=True)),
                ('maximum_beds', models.FloatField(blank=True)),
                ('furnished', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
