# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, null=True)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('short_name', models.CharField(max_length=200, null=True)),
                ('site_url', models.URLField(null=True)),
                ('currency', models.CharField(max_length=3, null=True)),
                ('connected', models.BooleanField()),
                ('geotargeting', models.BooleanField()),
                ('coupon_iframe_denied', models.BooleanField()),
                ('description', models.TextField(null=True)),
                ('cr', models.DecimalField(decimal_places=4, max_digits=4, null=True)),
                ('cr_trend', models.DecimalField(decimal_places=4, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CouponCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
