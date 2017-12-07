# -*- coding: utf-8 -*-
from base64 import b64encode
from django.conf import settings
import requests

def token():
    authorization = b64encode(settings.ADMINTAD_ID + ':' + settings.ADMINTAD_KEY)
    data = {
        'grant_type':'client_credentials',
        'client_id':settings.ADMINTAD_ID,
        'scope':'advcampaigns banners websites public_data coupons advcampaigns_for_website'
    }

    r = requests.post('https://api.admitad.com/token/', headers={'Authorization':'Basic '+authorization}, data=data)
    json = r.json()
    return json.get('access_token')

