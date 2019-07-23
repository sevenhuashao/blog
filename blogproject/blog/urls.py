#! /Users/huangsh/anaconda3/bin/ python
# encoding:utf-8
# @Time :2019/7/10 19:02


__author__ = 'Huangsh'


from django.conf.urls import url
from . import views

# app_name 为视图函数命名空间
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category')
]