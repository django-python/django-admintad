# -*- coding: utf-8 -*-
from admintad.api import authorization
from django.conf import settings
from admintad.models import CouponCategory


import requests

def categories():
    r = requests.get('https://api.admitad.com/coupons/categories/', headers={'Authorization':'Bearer '+authorization.token()}, params={'limit':500, 'offset':0})
    json = r.json()
    return json.get('results')

def list():
    r = requests.get('https://api.admitad.com/coupons/', headers={'Authorization':'Bearer '+authorization.token()}, params={'limit':1, 'offset':0})
    json = r.json()

    end = json.get('_meta').get('count') / 100
    for item in range(0,end):
        offset = str(item * 100)
        r = requests.get('https://api.admitad.com/coupons/', headers={'Authorization':'Bearer '+authorization.token()}, params={'limit':100, 'offset':offset})
        if r.status_code != 200:
            break

        for item in r.json().get('results'):
            #print item.get('status')
            #print item.get('rating')
            #print item.get('name')
            #print item.get('short_name')
            #print item.get('date_end')
            #print item.get('date_start')
            #print item.get('exclusive')
            #print item.get('discount')
            #print item.get('species')
            #print item.get('categories')
            print item.get('image')
            #print item.get('')


        break



def update():
    return list()
    
    create = []
    for item in categories():
        id   = item.get('id')
        name = item.get('name')

        try:
            CouponCategory.objects.get(pk=id)
        except CouponCategory.DoesNotExist:
            create.append(CouponCategory(pk=id, name=name))
        else:
            couponcategory = CouponCategory.objects.filter(pk=id)
            couponcategory.update(name=name)


    CouponCategory.objects.bulk_create(create)







        #print couponcategory

        #try:

        #except CouponCategory.DoesNotExist:
        #    print '11'
        #    couponcategory = CouponCategory(pk=item.get('id'), name=item.get('name'))
        #    couponcategory.save()
        #else:
            #couponcategory = CouponCategory.objects.filter(pk=item.get('id')).update(name=item.get('name'))
            #couponcategory.save()













     #   break




