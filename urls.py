from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'api/adv_campaign_site/categories/', views.adv_campaign_site_categories),
    url(r'api/adv_campaign_site/', views.adv_campaign_site),
]


