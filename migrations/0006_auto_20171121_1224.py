# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintad', '0005_auto_20171121_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advcampaign',
            name='cr',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True),
        ),
    ]
