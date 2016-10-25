# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='location_lat',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location_lon',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
    ]