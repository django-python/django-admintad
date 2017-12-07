# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class MetaRegion(models.Model):
    region = models.CharField(max_length=3)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.region

    class Meta:
        verbose_name_plural = _("Meta region")

class MetaCurrency(models.Model):
    code    = models.CharField(max_length=3)
    min_sum = models.DecimalField(max_digits=12, decimal_places=2)
    name    = models.CharField(max_length=100)
    sign    = models.CharField(max_length=5)

    def __unicode__(self):              # __unicode__ on Python 2
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = _("Meta currency")

class MetaTraffic(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):              # __unicode__ on Python 2
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = _("Meta traffic")

class MetaCategory(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return '%s' % (self.name)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = _("Meta category")

class MetaAction(models.Model):
    payment_size = models.CharField(max_length=100, null=True)
    name         = models.TextField()

    ACTION_TYPE = (
        (1, 'lead'),
        (2, 'sale'),
    )
    type   = models.IntegerField(choices=ACTION_TYPE, null=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return '%s %s' % (self.name,self.payment_size)

    class Meta:
        verbose_name_plural = _("Meta action")


class AdvCampaignRate(models.Model):
    hash          = models.CharField(max_length=40, null=True)
    name_tariff   = models.CharField(max_length=250)
    name_action   = models.CharField(max_length=250)
    size          = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    price_s       = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    is_percentage = models.NullBooleanField()

    def __unicode__(self):              # __unicode__ on Python 2
        return '%s %s' % (self.name_tariff, self.name_action)

    class Meta:
        verbose_name_plural = _("Adv campaign rates")


class AdvCampaignSite(models.Model):
    CONNECTION_STATUS = (
        (1, 'active'),
        (2, 'pending'),
        (3, 'declined'),
    )

    STATUS = (
        (1, 'active'),
        (2, 'disabled'),
    )

    name                 = models.CharField(max_length=250, null=True, verbose_name = _("Name"))
    image                = models.URLField(max_length=250, null=True, verbose_name = _("Image"))
    status             	 = models.IntegerField(choices=STATUS, null=True, verbose_name = _("Status"))
    connection_status	 = models.IntegerField(choices=CONNECTION_STATUS, null=True, verbose_name = _("Connection status"))
    rating               = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name = _("Rating"))
    description          = models.TextField(null=True, verbose_name = _("Description"))
    raw_description      = models.TextField(null=True, verbose_name = _("Raw description"))
    site_url             = models.URLField(max_length=400, null=True, verbose_name = _("Site URL"))
    currency             = models.ForeignKey(MetaCurrency, on_delete=models.CASCADE, null=True, verbose_name = _("Currency"))
    regions              = models.ManyToManyField(MetaRegion, verbose_name = _("Regions"))
    categories           = models.ManyToManyField(MetaCategory, verbose_name = _("Categories"))
    actions              = models.ManyToManyField(MetaAction, verbose_name = _("Actions"))
    rates                = models.ManyToManyField(AdvCampaignRate, verbose_name = _("Rates"))
    cr                   = models.DecimalField(max_digits=12, decimal_places=4, null=True, verbose_name = _("Сr"))
    ecpc                 = models.DecimalField(max_digits=12, decimal_places=4, null=True, verbose_name = _("Ecpc"))
    geotargeting         = models.NullBooleanField(verbose_name = _("Geotargeting"))
    coupon_iframe_denied = models.NullBooleanField(verbose_name = _("Coupon iframe denied"))
    activation_date      = models.DateTimeField(null=True, verbose_name = _("Activation date"))
    modified_date        = models.DateTimeField(null=True, verbose_name = _("Modified date"))
    avg_hold_time        = models.SmallIntegerField(null=True, verbose_name = _("Avg hold time"))
    gotolink             = models.CharField(max_length=250, null=True, verbose_name = _("Goto link"))
    goto_cookie_lifetime = models.SmallIntegerField(null=True, verbose_name = _("Goto cookie lifetime"))
    moderation           = models.NullBooleanField(verbose_name = _("Moderation"))
    traffics             = models.ManyToManyField(MetaTraffic, verbose_name = _("Traffics"))
    show_products_links  = models.NullBooleanField(verbose_name = _("Show products links"))
    products_xml_link	 = models.CharField(max_length=250, null=True, verbose_name = _("Products xml link"))
    products_csv_link	 = models.CharField(max_length=250, null=True, verbose_name = _("Products csv link"))

    def __unicode__(self):              # __unicode__ on Python 2
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = _("Adv campaign sites") # Список программ для сайта

