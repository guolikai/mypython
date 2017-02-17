#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2017-2-10 @Author:Guolikai'''

from django.shortcuts import render, redirect,render_to_response
from django.http.response import HttpResponse
#用于序列化Django的数据
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
import datetime
import models
from django.template.context_processors import request
# Create your views here.
#装饰器，需要做登录验证
def outer(func):
    def wrapper(request,*args,**kwargs):
        if not request.session.get('is_login'):
            return redirect('/login')
        else:
            return func(request,*args,**kwargs)
    return wrapper
    
def login(request):
    ret = {'status':''}
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        is_empty = all([username,password])
        if is_empty:
            count = models.User.objects.filter(username=username,password=password).count()
            if count==1:
               request.session['current_user']={'username':username}
               return redirect("/")
            else:
                ret['status'] = "用户名密码错误" 
            #try:
            #    currentObj = models.User.objects.get(username=username,password=password)
            #except Exception,e:
            #    currentObj = None
            #if  currentObj:
                #request.session['current_user_id']=currentObj.id
                #return redirect("/")
        else:
            ret['status'] = "用户名密码不能为空" 
    return render(request,"login.html",ret)

def logout(request):
    #销毁session值
    del request.session['current_user']
    return redirect('/login')

@outer
def index(request):
    ret = {'bbs_list':'','username':''}
    #user_dict = request.session.get('current_user',None)
    current_user = request.session.get('current_user',None)['username']
    ret['username'] = current_user
    bbs_list = models.News.objects.all()
    ret['bbs_list']=bbs_list
    return render(request,'index.html',ret)
    
def bbs_detail(request,bbs_id):
    bbs = models.News.objects.get(id=bbs_id)
    return render(request,'bbs_detail.html',{'bbs_obj':bbs,})

def addfavor(request):
    ret = {'status':0,'data':'','message':''}
    try:
        id = request.POST.get('nid')
        newsObj = models.News.objects.get(id=id)
        temp = newsObj.favor_count + 1
        newsObj.favor_count = temp
        newsObj.save()
        ret['status'] = 1
        ret['data'] = temp
    except Exception,e:
        ret['message'] = e.message    
    return HttpResponse(json.dumps(ret))

class CJSONEncoder(json.JSONEncoder):
    def default(self, obj):
       if isinstance(obj, datetime.datetime):
           return obj.strftime('%Y-%m-%d %H:%M:%S')
       elif isinstance(obj,datetime.date):
           return obj.strftime('%Y-%m-%d') 
       else:
           return json.JSONEncoder.default(self.obj)
       
       
    
def getreply(request):
    id = request.POST.get('nid')
    #newsObj = models.News.objects.get(id=id)
    #models.Reply.objects.filter(new=newsObj)
    reply_list = models.Reply.objects.filter(new_id=id).values('id','content','user__username','create_date')
    #reply_list=serializers.serialize("json",reply_list)
    #reply_list = json.dumps(list(reply_list),cls=DjangoJSONEncoder)
    reply_list = json.dumps(list(reply_list),cls=CJSONEncoder)
    return HttpResponse(reply_list)


def submitreply(request):
    ret = {'status':0,'data':'','message':'','count':''}
    try:
        id = request.POST.get('nid')
        data = request.POST.get('data') 
        current_user = request.session.get('current_user',None)['username']
        newObject = models.News.objects.get(id=id)
        userObject = models.User.objects.get(username=current_user)
        replyObj = models.Reply.objects.create(content=data,user=userObject,new=newObject)
        count  = models.Reply.objects.filter(new=models.News.objects.get(id=id)).count()
        newObject.reply_count = count
        newObject.save()
        #temp = {'content':replyObj.content,'user__username':replyObj.user.username,'create_date':replyObj.create_date}
        temp = {'content':replyObj.content,'user__username':replyObj.user.username,'create_date':replyObj.create_date.strftime('%Y-%m-%d %H:%M:%S')}
        ret['status'] = 1
        ret['count'] = count
        ret['data'] = temp
    except Exception,e:
        ret['message'] = e.message  
    #ret = json.dumps(ret,cls=DjangoJSONEncoder)    
    #return HttpResponse(ret)    
    return HttpResponse(json.dumps(ret)) 
        
        
def submitchat(request):
    ret = {'status':0,'data':'','message':''}
    try:
        value = request.POST.get('data') 
        current_user = request.session.get('current_user',None)['username']
        userObj = models.User.objects.get(username=current_user)
        chatObj = models.Chat.objects.create(content=value,user=userObj)
        ret['status'] = 1
        temp = {#'content':chatObj.content,
                'id':chatObj.id,
                'username':chatObj.user.username,
                'create_date':chatObj.create_date.strftime('%Y-%m-%d %H:%M:%S')}
        ret['data'] = temp
    except Exception,e:
        ret['message'] = e.message 
    return HttpResponse(json.dumps(ret)) 


def getchat(request):
    charList = models.Chat.objects.all().order_by('-id')[0:10].values('id','content','user__username','create_date')
    charList = json.dumps(list(charList),cls=CJSONEncoder)
    return HttpResponse(charList)
    
def getchat2(request):
    
    last_id = request.POST.get('lastid') 
    charList = models.Chat.objects.filter(id_gt=last_id).values('id','content','user__username','create_date')
    charList = json.dumps(list(charList),cls=CJSONEncoder)
    return HttpResponse(charList)
