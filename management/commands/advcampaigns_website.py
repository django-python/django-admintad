# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from admintad.api import authorization, advcampaign, meta
import requests
 
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        meta.update()
        advcampaign.advcampaigns_website()
        #coupon.update()


