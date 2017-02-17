#!/usr/bin/env python
#_*_coding:utf8 _*_
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from web.models import Hostname
from django.template.context_processors import request
from web.models import UserInfo
from web.forms import RegisterForm
# Create your views here.
def index(resuest):
    return HttpResponse('index')

def Login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        print user,pwd
        #result = UserInfo.objects.filter(username=user,password=pwd).count()
        if user =='glk' and pwd =='123456':
            return HttpResponse('登录成功')
        else:
            return render_to_response('login.html',{'stutus':'用户名密码错误'})
    else:
        return render_to_response('login.html')

def Register(request):
    registerform = RegisterForm()
    if request.method == 'POST':
        form_data = RegisterForm(request.POST)
        if form_data .is_valid():
            data = form_data .cleaned_data
            print data
        else:
            print form_data .errors
    return render_to_response('register.html',{'form':registerform})

def Add(request,hostname):
    Hostname.objects.create(hostname=hostname)
    return HttpResponse('Add ok')

def Delete(request,id):
    Hostname.objects.get(id=id).delete()
    return HttpResponse('Delete ok')

def UpdateOne(request,id,hostname):
    obj = Hostname.objects.get(id=id)
    obj.hostaname = hostname
    obj.save()
    return HttpResponse('Update ok')

def UpdateFilter(request,id,hostname):
    hostname.object.filter(id__gt=id).update(hostname=hostname)
    return HttpResponse('Update ok')

def Get(request,hostname):
    data = hostname.object.filter(hostname__contains=hostname)
    print data.query
    for item in data:
        print item.id
    return HttpResponse('Get ok')
def HostnameList(request):
    hostname_list = Hostname.objects.all()
    result = render_to_response('hostname.html',{'data':hostname_list,'system':'Host Manager'})
    return result

    