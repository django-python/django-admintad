# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advcampaign',
            name='cr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='advcampaign',
            name='cr_trend',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
