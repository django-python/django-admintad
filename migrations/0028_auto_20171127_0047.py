# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintad', '0027_metacategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metacategory',
            options={'verbose_name_plural': 'Meta category'},
        ),
        migrations.AlterModelOptions(
            name='metacurrency',
            options={'verbose_name_plural': 'Meta currency'},
        ),
        migrations.AlterModelOptions(
            name='metaregion',
            options={'verbose_name_plural': 'Meta region'},
        ),
        migrations.AlterModelOptions(
            name='metatraffic',
            options={'verbose_name_plural': 'Meta traffic'},
        ),
        migrations.AddField(
            model_name='advcampaign',
            name='regions',
            field=models.ManyToManyField(to='admintad.MetaRegion'),
        ),
    ]