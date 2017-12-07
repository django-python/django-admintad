# -*- coding: utf-8 -*-
from admintad.api import authorization
from django.conf import settings
from admintad.models import MetaRegion, MetaCurrency, MetaTraffic, MetaCategory

import requests

def update():
    token = authorization.token()

    # Update categories
    r = requests.get('https://api.admitad.com/categories/', headers={'Authorization':'Bearer '+token}, params={'limit':500, 'offset':0})
    json = r.json()

    for item in json.get('results'):
        if not item.get('parent'):
            MetaCategory.objects.update_or_create(id=item.get('id'), defaults={'name':item.get('name')})

    for item in json.get('results'):
        if item.get('parent'):
            parent = MetaCategory.objects.get(pk=item.get('parent').get('id'))
            MetaCategory.objects.update_or_create(id=item.get('id'), defaults={'name':item.get('name')}, parent=parent)


    # Update regions
    r = requests.get('https://api.admitad.com/websites/regions/', headers={'Authorization':'Bearer '+token}, params={'limit':500, 'offset':0})
    json = r.json()

    for region in json.get('results'):
        obj, created = MetaRegion.objects.update_or_create(region=region)


    # Update currencies
    r = requests.get('https://api.admitad.com/currencies/', headers={'Authorization':'Bearer '+token}, params={'limit':500, 'offset':0})
    json = r.json()

    for item in json.get('results'):
        obj, created = MetaCurrency.objects.update_or_create(code=item.get('code'), defaults={'min_sum':item.get('min_sum'), 'name':item.get('name'), 'sign':item.get('sign')})

    # Update traffics
    r = requests.get('https://api.admitad.com/traffic/', headers={'Authorization':'Bearer '+token}, params={'limit':500, 'offset':0})
    json = r.json()
    for item in json.get('results'):
        obj, created = MetaTraffic.objects.update_or_create(id=item.get('id'), defaults={'name':item.get('name')})


    return json.get('results')


