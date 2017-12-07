# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from .models import AdvCampaignSite, AdvCampaignRate, MetaRegion, MetaCategory, MetaTraffic, MetaCurrency, MetaAction

def adv_campaign_site_categories(request):
    data = {'list':[]}

    categories = MetaCategory.objects.filter(level__in=[0])
    for category in categories:

        children = []
        for child in category.get_children():
            children.append({'name':child.name, 'id':child.id})

        data['list'].append({'name':category.name, 'id':category.id, 'children':children})

    return JsonResponse(data)

def adv_campaign_site(request):

    data = {'list':[]}
    sites = AdvCampaignSite.objects.all()
    for site in sites:

        json = {
            'id':site.id,
            'name':site.name,
            'image':site.image,
            'status':site.status,
            'connection_status':site.connection_status,
            'rating':site.rating,
            #'description':site.description,
            #'raw_description':site.raw_description,
            'site_url':site.site_url,
            'currency':{
                'code':site.currency.code,
                'name':site.currency.name,
                'min_sum':site.currency.min_sum,
                'sign':site.currency.sign,
            },
            'cr':site.cr,
            'ecpc':site.ecpc,
            'geotargeting':site.geotargeting,
            'coupon_iframe_denied':site.coupon_iframe_denied,
            'activation_date':site.activation_date,
            'modified_date':site.modified_date,
            'avg_hold_time':site.avg_hold_time,
            'gotolink':site.gotolink,
            'goto_cookie_lifetime':site.goto_cookie_lifetime,
            'moderation':site.moderation,
            'show_products_links':site.show_products_links,
            'products_xml_link':site.products_xml_link,
            'products_csv_link':site.products_csv_link,

            'regions':[],
            'rates':[],
            'categories':[],
        }

        if json['status'] == 1:
            json['status'] = 'active'
        else:
            json['status'] = 'disabled'

        if json['connection_status'] == 1:
            json['connection_status'] = True
        else:
            json['connection_status'] = False

        for region in site.regions.all():
            json['regions'].append(region.region)

        rates = []
        for rate in site.rates.all():
            json['rates'].append({
                'tariff':rate.name_tariff,
                'action':rate.name_action,
                'size':rate.size,
                'price_s':rate.price_s,
                'is_percentage':rate.is_percentage,
            })

            if rate.is_percentage == True:
                rates.append(rate.size)


        rates = sorted(rates)
        if len(rates) > 0:
            json['rate'] = rates[0]
        else:
            json['rate'] = None


        for category in site.categories.all():
            json['categories'].append(category.id)


        data['list'].append(json)

    return JsonResponse(data)

