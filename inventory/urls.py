# from django.conf.urls import patterns, include, url
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
from django.urls import path, include
from kucun.views import all_phone
urlpatterns = [
    path('^admin/',  admin.site.urls),
    path('', all_phone),
    path('kucun/', include('kucun.urls')),
    path('sell/', include('sell.urls')),
    path('weixin/', include('weixin.urls')),
    path('meizu/', include('meizu.urls')),
]
