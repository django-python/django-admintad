# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintad', '0030_advcampaign_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advcampaign',
            name='site_url',
            field=models.URLField(null=True, verbose_name='Site URL'),
        ),
        migrations.AlterField(
            model_name='advcampaign',
            name='status',
            field=models.CharField(max_length=200, null=True, verbose_name='Status'),
        ),
    ]
