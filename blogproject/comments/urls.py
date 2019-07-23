#! /Users/huangsh/anaconda3/bin/ python
# encoding:utf-8
# @Time :2019/7/22 18:22


__author__ = 'Huangsh'

from django.conf.urls import url
from . import views


app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
]