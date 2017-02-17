#!/usr/bin/env python 
# _*_coding:utf8 _*_
'''Created on 2016��12��18��  @author: lenovo'''
from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)