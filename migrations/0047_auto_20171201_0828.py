# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintad', '0046_auto_20171130_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advcampaignrate',
            name='name_action',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='advcampaignrate',
            name='name_tariff',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='advcampaignrate',
            name='price_s',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='advcampaignrate',
            name='size',
            field=models.CharField(max_length=250),
        ),
    ]
