# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintad', '0034_advcampaign_actions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metaaction',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
