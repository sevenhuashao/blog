#! /Users/huangsh/anaconda3/bin/ python
# encoding:utf-8
# @Time :2019/7/22 17:33


__author__ = 'Huangsh'


from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']