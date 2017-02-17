#/usr/bin/env python
#coding:utf-8


from django.shortcuts import render, render_to_response, redirect
from operator import is_
from django.template.context import RequestContext
from django.template.context_processors import csrf

# Create your views here.
def index(request):
    #获取session值
    user_dict = request.session.get('is_login',None)
    if  user_dict:
        return render_to_response('app02/index.html',{'username':user_dict['user']})
    else:    
        return redirect('/app02/login/')

def login(request):
    c ={}
    c.update(csrf(request))
    if request.method =='POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        if user=='glk' and pwd == '123456':
            #设置session值，默认过期时间2周
            request.session['is_login']={'user':user}
            return redirect('/app02/index/')
        else:
            #return render_to_response('app02/login.html',{'data':'error'},RequestContext(request))
        
    #return render_to_response('app02/login.html',RequestContext(request))
            return render_to_response('app02/login.html',{'data':'error'},c)
        
    return render_to_response('app02/login.html',c)

def logout(request):
    #销毁session值
    del request.session['is_login']
    return redirect('/app02/login/')
    
    