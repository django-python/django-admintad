# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from .models import AdvCampaignSite, AdvCampaignRate, MetaRegion, MetaCategory, MetaTraffic, MetaCurrency, MetaAction

admin.site.site_header = 'Administration Admintad'

class MetaRegionAdmin(admin.ModelAdmin):
    list_display = ('region',)
    readonly_fields=('region', )
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class MetaCategoryAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
    list_display = ('name',)
    readonly_fields = ('name', 'parent', )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class MetaTrafficAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields=('name', )
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class MetaCurrencyAdmin(admin.ModelAdmin):
    list_display = ('name','code', 'min_sum', 'sign')
    readonly_fields=('name','code', 'min_sum', 'sign', )

    actions = None
    #list_filter = ('connected',)
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    #def has_change_permission(self, request, obj=None):
    #    return False

class MetaActionAdmin(admin.ModelAdmin):
    list_display = ('name','payment_size','type')
    readonly_fields=('name','payment_size','type')
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class AdvCampaignSiteAdmin(admin.ModelAdmin):
    list_display = ('name','rating','connection_status','status')
    list_filter = ('status',)
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class AdvCampaignRateAdmin(admin.ModelAdmin):
    list_display = ('name_tariff','name_action','size', 'price_s', 'is_percentage')
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(MetaRegion, MetaRegionAdmin)
admin.site.register(MetaCategory, MetaCategoryAdmin)
admin.site.register(MetaTraffic, MetaTrafficAdmin)
admin.site.register(MetaCurrency, MetaCurrencyAdmin)
admin.site.register(MetaAction, MetaActionAdmin)
admin.site.register(AdvCampaignSite, AdvCampaignSiteAdmin)
admin.site.register(AdvCampaignRate, AdvCampaignRateAdmin)

