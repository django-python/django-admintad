# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintad', '0025_auto_20171121_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaTraffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]