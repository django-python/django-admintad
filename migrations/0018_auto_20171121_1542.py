# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintad', '0017_auto_20171121_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advcampaign',
            name='cr',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='advcampaign',
            name='cr_trend',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
    ]
