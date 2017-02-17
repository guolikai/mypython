#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-20 @Author:Guolikai'''
from django import forms
from django.template.defaulttags import widthratio
from django.forms.widgets import Widget

class Alogin(forms.Form):
    username = forms.CharField(error_messages={'required':('用户名不能为空'),'invalid':('用户名格式不对')})
    email = forms.EmailField(error_messages={'required':('邮箱不能为空'),'invalid':('邮箱格式不对')})
    ip = forms.GenericIPAddressField(error_messages={'required':('IP不能为空'),'invalid':('IP格式不对')})