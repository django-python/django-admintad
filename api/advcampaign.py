# -*- coding: utf-8 -*-
from admintad.api import authorization
from django.conf import settings
from admintad.models import AdvCampaignSite, AdvCampaignRate
from admintad.models import MetaRegion, MetaCurrency, MetaTraffic, MetaCategory, MetaRegion, MetaAction
import requests, re, hashlib

try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode


def advcampaigns_website():
    token = authorization.token()
    r = requests.get('https://api.admitad.com/advcampaigns/website/'+str(settings.ADMINTAD_SITE_ID)+'/', headers={'Authorization':'Bearer '+token}, params={'limit':1, 'offset':0})
    json = r.json()

    end = (json.get('_meta').get('count') / 100) + 100
    for item in range(0,end):
        offset = str(item * 100)
        r = requests.get('https://api.admitad.com/advcampaigns/website/'+str(settings.ADMINTAD_SITE_ID)+'/', headers={'Authorization':'Bearer '+token}, params={'limit':100, 'offset':offset})
        if r.status_code != 200:
            break

        for item in r.json().get('results'):
            if not item.get('activation_date'):
                item['activation_date'] = '2000-01-01T00:00:00'

            if item.get('connection_status') == 'active':
                item['connection_status'] = 1
            elif item.get('connection_status') == 'pending':
                item['connection_status'] = 2
            else:
                item['connection_status'] = 3

            if item.get('status') == 'active':
                item['status'] = 1
            else:
                item['status'] = 2


            currency = MetaCurrency.objects.get(code=item.get('currency'))

            url_parts = list(urlparse.urlparse(item.get('image')))
            url_parts[0] = 'https'
            item['image'] = urlparse.urlunparse(url_parts)

            defaults = {
                'name':item.get('name'),
                'image':item.get('image'),
                'status':item.get('status'),
                'connection_status':item.get('connection_status'),
                'rating':item.get('rating'),
                'description':item.get('description'),
                'raw_description':item.get('raw_description'),
                'site_url':item.get('site_url'),
                'currency':currency,
                'cr':item.get('cr'),
                'ecpc':item.get('ecpc'),
                'geotargeting':item.get('geotargeting'),
                'coupon_iframe_denied':item.get('coupon_iframe_denied'),
                'activation_date':item.get('activation_date')+'+03',
                'modified_date':item.get('modified_date')+'+03',
                'avg_hold_time':item.get('avg_hold_time'),
                'gotolink':item.get('gotolink'),
                'goto_cookie_lifetime':item.get('goto_cookie_lifetime'),
                'moderation':item.get('moderation'),
                'show_products_links':item.get('show_products_links'),
                'products_xml_link':item.get('products_xml_link'),
                'products_csv_link':item.get('products_csv_link'),
            }
            
            campaign, created = AdvCampaignSite.objects.update_or_create(id=item.get('id'), defaults=defaults)

            # Actions Detail
            campaign.rates.clear()

            for actions_detail in item.get('actions_detail'):
                for tariff in actions_detail.get('tariffs'):
                    id = str(tariff.get('id')) + '' + str(tariff.get('action_id'))
                    
                    for rate in tariff.get('rates'):
                        m = hashlib.sha1()
                        m.update(str(id) + str(rate.get('id')))

                        defaults = {
                            'name_action':actions_detail.get('name'),
                            'name_tariff':tariff.get('name'),
                            'size':rate.get('size'), # Размер ставки (процент или сумма в валюте кампании)
                            'is_percentage':rate.get('is_percentage'), # Тип ставки (True если процентная)
                            'price_s':rate.get('price_s'),
                        }

                        rate, created = AdvCampaignRate.objects.update_or_create(hash=m.hexdigest(), defaults=defaults)
                        campaign.rates.add(rate)


            # Regions
            regions = map(lambda x: x.get('region'), item.get('regions'))
            regions = MetaRegion.objects.filter(region__in=regions)
            campaign.regions.clear()
            for region in regions:
                campaign.regions.add(region)


            # Categories
            categories = map(lambda x: x.get('id'), item.get('categories'))
            categories = MetaCategory.objects.filter(pk__in=categories)
            campaign.categories.clear()
            for category in categories:
                campaign.categories.add(category)


            # Traffics
            traffic_list = []
            for traffic in item.get('traffics'):
                if traffic.get('enabled') == True:
                    traffic_list.append(traffic.get('id'))

            traffics = MetaTraffic.objects.filter(pk__in=traffic_list)
            campaign.traffics.clear()
            for traffic in traffics:
                campaign.traffics.add(traffic)


            # Actions
            for action in item.get('actions'):
                if action.get('type') == 'lead':
                    action_type = 1
                else:
                    action_type = 2

                defaults = {
                    'name':action.get('name'),
                    'payment_size':action.get('payment_size'),
                    'type':action_type,
                }
                action_obj, created = MetaAction.objects.update_or_create(pk=action.get('id'), defaults=defaults)
                campaign.actions.add(action_obj)



            #break
        #break



#https://api.admitad.com/advcampaigns/website/{w_id}/

def update():
    token = authorization.token()

    r = requests.get('https://api.admitad.com/advcampaigns/', headers={'Authorization':'Bearer '+token}, params={'limit':1, 'offset':0})
    json = r.json()

    end = json.get('_meta').get('count') / 100
    for item in range(0,end):
        offset = str(item * 100)
        r = requests.get('https://api.admitad.com/advcampaigns/', headers={'Authorization':'Bearer '+token}, params={'limit':100, 'offset':offset})
        if r.status_code != 200:
            break

        for item in r.json().get('results'):
            if not item.get('activation_date'):
                item['activation_date'] = '2000-01-01T00:00:00'

            if item.get('action_type') == 'lead':
                action_type = 1
            else:
                action_type = 2

            defaults = {
                'status':item.get('status'),
                'rating':item.get('rating'),
                'name':item.get('name'),
                'short_name':item.get('short_name'),
                'site_url':item.get('site_url'),
                'image':item.get('image'),
                'currency':item.get('currency'),
                'connected':item.get('connected'),
                'description':item.get('description'),
                'geotargeting':item.get('geotargeting'),
                'cr':item.get('cr'),
                'cr_trend':item.get('cr_trend'),
                'ecpc':item.get('ecpc'),
                'ecpc_trend':item.get('ecpc_trend'),
                'rate_of_approve':item.get('rate_of_approve'),
                'more_rules':item.get('more_rules'),
                'activation_date':item.get('activation_date')+'+03',
                'modified_date':item.get('modified_date')+'+03',
                'avg_hold_time':item.get('avg_hold_time'),
                'denynewwms':item.get('denynewwms'),
                'goto_cookie_lifetime':item.get('goto_cookie_lifetime'),
                'action_type':action_type,
            }
            
            obj, created = AdvCampaign.objects.update_or_create(id=item.get('id'), defaults=defaults)

            # Regions
            regions = map(lambda x: x.get('region'), item.get('regions'))
            regions = MetaRegion.objects.filter(region__in=regions)
            obj.regions.clear()
            for region in regions:
                obj.regions.add(region)

            # Traffics
            traffic_list = []
            for traffic in item.get('traffics'):
                if traffic.get('enabled') == True:
                    traffic_list.append(traffic.get('id'))


            traffics = MetaTraffic.objects.filter(pk__in=traffic_list)
            obj.traffics.clear()
            for traffic in traffics:
                obj.traffics.add(traffic)

            # Categories
            categories = map(lambda x: x.get('id'), item.get('categories'))
            categories = MetaCategory.objects.filter(pk__in=categories)
            obj.categories.clear()
            for category in categories:
                obj.categories.add(category)

            # Actions
            for action in item.get('actions'):

                if action.get('type') == 'lead':
                    action_type = 1
                else:
                    action_type = 2

                defaults = {
                    'name':action.get('name'),
                    'payment_size':action.get('payment_size'),
                    'type':action_type,
                }

                action_obj, created = MetaAction.objects.update_or_create(pk=action.get('id'), defaults=defaults)
                obj.actions.add(action_obj)

            #break

        #break

