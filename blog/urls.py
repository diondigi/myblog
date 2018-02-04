#!/usr/bin/env python
#---coding:utf-8---
#__auther__:Administrator
# date : 2018/1/30
from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^abc/$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives, name='archives')
]