"""
Definition of urls for FightingFowl.
"""
from django.conf.urls import include, url
from StockerChecker import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form/parse_json$', views.parse_json, name='parse_json'),
]
