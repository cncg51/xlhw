# -*- coding: utf-8 -*-

# from django.conf.urls import patterns, url
from django.urls import path, include, re_path
from weixin import views as weixin_views

__author__ = 'JiaPan'

urlpatterns = [
    re_path(r'^$', weixin_views.handleRequest),
    re_path(r'^contact/$', weixin_views.contact),
    re_path(r'^send_dynamic/(?P<openid>.*?)/(?P<phone>\d+)/$',
            weixin_views.send_dynamic),
    re_path(r'^register/success/$', weixin_views.register_success,
            name='register_success'),
    re_path(r'^register/already/$', weixin_views.register_already,
            name='register_already'),
    re_path(r'^register/(?P<openid>.*?)/$', weixin_views.register),
]
