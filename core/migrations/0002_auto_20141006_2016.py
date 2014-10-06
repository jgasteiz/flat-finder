# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='lat_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='lat_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='lon_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='lon_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='maximum_beds',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='maximum_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='minimum_beds',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='minimum_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='radius',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
