# -*- coding: utf-8 -*-
# from django.conf.urls import patterns, url
from django.urls import path, include
from sell import views as sell_views
__author__ = 'JiaPan'

urlpatterns = [

    path('', sell_views.index),

]
