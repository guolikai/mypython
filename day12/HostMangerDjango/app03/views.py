#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-20 @Author:Guolikai'''
from django.shortcuts import render
from django.shortcuts import render_to_response
from app03 import forms
# Create your views here.
def Login(request):
    ret = {'data':'','error':''}
    obj = forms.Alogin()
    ret['data']= obj
    if request.method=='POST':
        checkForm = forms.Alogin(request.POST)
        checkresult = checkForm.is_valid()
        if checkresult:
            pass
        else:
            firstErrorMsg = checkForm.errors.as_data().values()[0][0].message[0]
            ret['error']=firstErrorMsg
            print checkForm.errors.as_data().values()[0][0]
            ret['data'] = checkForm
    return  render_to_response('app03/login.html', ret)
    
    