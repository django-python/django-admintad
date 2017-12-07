# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintad', '0023_metacurrency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metacurrency',
            name='min_sum',
            field=models.DecimalField(decimal_places=4, max_digits=12),
        ),
    ]
