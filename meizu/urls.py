# -*- coding: utf-8 -*-
# from django.conf.urls import patterns, url
from django.urls import path, include, re_path
from meizu import views as meizu_views
__author__ = 'JiaPan'
app_name = 'meizu'

urlpatterns = [
    re_path(r'^$', meizu_views.all_phone),
    re_path(r'^all/phone/$', meizu_views.all_phone, name='meizu_allphone'),
    re_path(
        r'^guoao/phone/$', meizu_views.guoao_phone, name='meizu_guoaophone'),
    re_path(
        r'^dadian/phone/$', meizu_views.dadian_phone,
        name='meizu_dadianphone'),
    re_path(
        r'^hongwei/phone/$',
        meizu_views.hongwei_phone,
        name='meizu_hongweiphone'),
    re_path(
        r'^all/peijian/$', meizu_views.all_peijian, name='meizu_allpeijian'),
    re_path(
        r'^guoao/peijian/$',
        meizu_views.guoao_peijian,
        name='meizu_guoaopeijian'),
    re_path(
        r'^dadian/peijian/$',
        meizu_views.dadian_peijian,
        name='meizu_dadianpeijian'),
    re_path(
        r'^hongwei/peijian/$',
        meizu_views.hongwei_peijian,
        name='meizu_hongweipeijian'),
    re_path(r'^add/$', meizu_views.add_goods, name="meizu_addgoods"),
    re_path(r'^login/$', meizu_views.mylogin, name='meizu_mylogin'),
    re_path(r'^login/fail$', meizu_views.login_fail, name='meizu_login_fail'),
    re_path(r'^logout/$', meizu_views.mylogout, name="meizu_logout"),
    re_path(
        r'^add/success/$', meizu_views.add_success, name="meizu_addsuccess"),
    re_path(r'^api/remain/$', meizu_views.api_remain, name="meizu_api_remain"),
    re_path(r'^api/diaoku/$', meizu_views.api_diaoku, name="meizu_api_diaoku"),
    re_path(r'^api/update/$', meizu_views.api_update, name="meizu_api_update"),
    re_path(
        r'^api/delete_goods_record/$',
        meizu_views.api_delete_goods_record,
        name="meizu_api_delete_goods_record"),
    re_path(
        r'^api/delete_goods/$',
        meizu_views.delete_goods,
        name="meizu_api_delete_goods"),
    re_path(
        r'^api/setcolor/$',
        meizu_views.api_setcolor,
        name="meizu_api_setcolor"),
    re_path(
        r'^api/showcolor/$',
        meizu_views.api_showcolor,
        name="meizu_api_showcolor"),
    re_path(r'^outin/$', meizu_views.out_in, name="meizu_out_in"),
    re_path(
        r'^checkoutin/$', meizu_views.check_out_in, name="meizu_check_out_in"),
    re_path(r'^transfer/$', meizu_views.transfer, name="meizu_transfer"),
    re_path(
        r'^changeprice/$', meizu_views.change_price,
        name="meizu_change_price"),
    re_path(
        r'^return_record/$',
        meizu_views.return_record,
        name="meizu_return_record"),
    re_path(
        r'^checkbackup/$', meizu_views.check_backup,
        name="meizu_check_backup"),
    re_path(r'^backup/$', meizu_views.mybackup, name="meizu_backup"),
    re_path(
        r'^delete_goods/$',
        meizu_views.delete_goods,
        name="meizu_delete_goods"),

    # re_path(r'^modal/diaoku/$', meizu_views.modal_diaoku', name="modal_diaoku"),
    re_path(
        r'^chart/sell_ranking/$',
        meizu_views.sell_ranking_chart,
        name="meizu_sell_ranking_chart"),
    re_path(
        r'^single_goods_detail/$',
        meizu_views.single_goods_detail,
        name="meizu_single_goods_detail"),
]
