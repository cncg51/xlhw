# -*- coding: utf-8 -*-
# from django.conf.urls import patterns, url
from django.urls import path, include
from kucun import views  as kucun_views

__author__ = 'JiaPan'

urlpatterns = [
    path('', kucun_views.all_phone),

    path('all/phone/', kucun_views.all_phone, name='allphone'),
    path('guoao/phone/', kucun_views.guoao_phone, name='guoaophone'),
    path('dadian/phone/', kucun_views.dadian_phone, name='dadianphone'),
    path('hongwei/phone/', kucun_views.hongwei_phone, name='hongweiphone'),

    path('all/peijian/', kucun_views.all_peijian, name='allpeijian'),
    path('guoao/peijian/', kucun_views.guoao_peijian, name='guoaopeijian'),
    path('dadian/peijian/', kucun_views.dadian_peijian, name='dadianpeijian'),
    path('hongwei/peijian/', kucun_views.hongwei_peijian, name='hongweipeijian'),

    path('add/', kucun_views.add_goods, name="addgoods"),
    path('login/', kucun_views.mylogin, name='mylogin'),
    path('login/fail', kucun_views.login_fail, name='login_fail'),
    path('logout/', kucun_views.mylogout, name="logout"),
    path('add/success/', kucun_views.add_success, name="addsuccess"),

    path('api/remain/', kucun_views.api_remain, name="api_remain"),
    path('api/diaoku/', kucun_views.api_diaoku, name="api_diaoku"),
    path('api/update/', kucun_views.api_update, name="api_update"),
    path('api/delete_goods_record/', kucun_views.api_delete_goods_record,
         name="api_delete_goods_record"),
    path('api/delete_goods/', kucun_views.delete_goods,
         name="api_delete_goods"),
    path('api/setcolor/', kucun_views.api_setcolor, name="api_setcolor"),
    path('api/showcolor/', kucun_views.api_showcolor, name="api_showcolor"),


    path('outin/', kucun_views.out_in, name="out_in"),
    path('checkoutin/', kucun_views.check_out_in, name="check_out_in"),
    path('transfer/', kucun_views.transfer, name="transfer"),
    path('changeprice/', kucun_views.change_price, name="change_price"),
    path('return_record/', kucun_views.return_record, name="return_record"),

    path('checkbackup/', kucun_views.check_backup, name="check_backup"),
    path('backup/', kucun_views.mybackup, name="backup"),

    path('delete_goods/', kucun_views.delete_goods, name="delete_goods"),

    # path('modal/diaoku/', kucun_views.modal_diaoku, name="modal_diaoku"),
    path('chart/sell_ranking/', kucun_views.sell_ranking_chart,
         name="sell_ranking_chart"),

    path('single_goods_detail/', kucun_views.single_goods_detail,
         name="single_goods_detail"),
]
