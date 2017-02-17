#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-20 @Author:Guolikai'''

from django.shortcuts import render, redirect,render_to_response
from django.http.response import HttpResponse
from django.core.paginator import Page
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template.context_processors import csrf

from web import models
from web import common
from web import html_helper

#装饰器，需要做登录验证
def outer(func):
    def wrapper(request,*args,**kwargs):
        if not request.session.get('is_login'):
            return redirect('/web/login.html')
        else:
            return func(request,*args,**kwargs)
    return wrapper
'''
def outer(func):
    def wrapper(request,*args,**kwargs):
        if not request.session.get('is_login'):
            return redirect('/web/login.html')
        else:
            return func(request,*args,**kwargs)
    return wrapper
#自定义装饰器
def Filter(before_func,after_func):
    def Outer(main_func):
        def wrapper(request,*args,**kwargs):
            
            before_result = before_func(request,*args,**kwargs)
            if(before_result != None):
                return before_result;
            
            main_result = before_func(request,*args,**kwargs)
            if(main_result != None):
                return main_result;
            
            after_result = before_func(request,*args,**kwargs)
            if(after_result != None):
                return after_result;
        return wrapper    
    return Outer       
            '''
            
@outer
def Index(request,*args,**kwargs):
    user_dict = request.session.get('is_login',None)
    #return render(request,'web/index.html',{'username':request.session.get('is_login')['user']})
    return render(request,'web/index.html',{'username':user_dict['user']})


def Login(request):
    ret = {'status':''}
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        is_empty = all([username,password])
        if is_empty:
            count = models.UserInfo.objects.filter(username=username,password=password).count()
            if count==1:
                request.session['is_login']={'user':username}
                return redirect("/web/index.html")
            else:
                ret['status'] = "用户名密码错误" 
        else:
            ret['status'] = "用户名密码不能为空" 
    return render(request,"web/login.html",ret)

def Logout(request):
    #销毁session值
    del request.session['is_login']
    return redirect('/web/login.html')

@csrf_exempt
def Register(request):
    ret = {'status':'','usertype':None}
    '''
    #创建用户类型
    t1 = models.UserType.objects.create(typename="超级管理员")
    t2 = models.UserType.objects.create(typename="普通管理员")
    t3 = models.UserType.objects.create(typename="普通用户")
    #创建用户
    u1 = models.UserInfo.objects.create(username='user01',
                                        password='123456',
                                        email='user01@sina.com',
                                        user_type=t1)
    u2 = models.UserInfo.objects.create(username='user02',
                                        password='123456',
                                        email='user02@sina.com',
                                        user_type=t2)
    #创建用户组
    groupobj = models.UserGroup.objects.create(groupname='监控组')
    groupobj = models.UserGroup.objects.create(groupname='开发组')
    groupobj = models.UserGroup.objects.create(groupname='管理组')
    groupobj = models.UserGroup.objects.create(groupname='运维组')
    groupobj.user.add(u1)
    groupobj.user.add(u2)'''
    usertype = models.UserType.objects.all()
    ret['usertype'] = usertype
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        email = request.POST.get('email',None)
        usertype_id = request.POST.get('usertype',None)
        is_empty = all([username,password,email])
        if is_empty:
            usertypeobj = models.UserType.objects.get(id=usertype_id)
            models.UserInfo.objects.create(username=username,
                                        password=password,
                                        email=email,
                                        user_type=usertypeobj)
            ret['status']="注册成功"
            return redirect("/web/login.html")
        else:
            ret['status'] = "Username、Password、Email不能为空"     
    return render(request,"web/register.html",ret)

@outer
def host_add(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':None,'group':None,'username':user_dict['user']}
    usergroup = models.UserGroup.objects.all()
    ret['group'] = usergroup
    if request.method == 'POST':
        hostname = request.POST.get('hostname',None)
        ip = request.POST.get('ip',None)
        group_id = request.POST.get('group',None)
        is_empty = all([hostname,ip])
        if is_empty:
            #多表插入：获取包含(1 **管理员)的对象，对象对应的类是UserGroup
            groupobj = models.UserGroup.objects.get(id=group_id)
            models.Asset.objects.create(hostname=hostname,
                                        ip=ip,
                                        user_group=groupobj)
            ret['status']="添加成功"
            return redirect("/web/index.html",ret)
        else:
            ret['status'] = "Hostname或Ip不能为空" 
    #获取所有数据                   
    data = models.Asset.objects.all()
    ret['data'] = data
    #根据UserGroup中的groupname获取对应的数据
    #data = models.Asset.objects.filter(user_group__groupname=u'监控组')
    #data = models.Asset.objects.filter(user_group__id=1)
    #for item in data:
    #    print item
    
    return render(request,"web/host_add.html",ret)
'''def List(request):
    ret = {'data':None}
    data = models.Asset.objects.all()
    ret['data'] = data
    return render(request,"web/host_list.html",ret)
    '''
@outer
def Host_list(request,page):
    user_dict = request.session.get('is_login',None)
    per_item = common.try_int(request.COOKIES.get('pager_num',10),10)
    #操作数据库进行分页
    page = common.try_int(page,1)
    count = models.Asset.objects.all().count()
    pageobj =  html_helper.PageInfo(page,count,per_item)
    result = models.Asset.objects.all()[pageobj.start:pageobj.end]
    page_string = html_helper.Pager(page,pageobj.pages_all_count)
    ret = {'data':result,'count':count,'page':page_string,'username':user_dict['user']}
    response = render(request,'web/host_list.html',ret)
    response.set_cookie('pager_num',per_item)
    return response

@outer
def host_del(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    if request.method == 'POST':
        hostname = request.POST.get('hostname',None)
        is_empty = all([hostname])
        if is_empty:
            count = models.Asset.objects.filter(hostname=hostname).count()
            if count==0:
                ret['status'] = "用户组不存在"
            else:    
                models.Asset.objects.get(hostname=hostname).delete()
                ret['status']="用户组删除成功"
                return redirect("/web/host_del.html")
        else:
            ret['status'] = "用户组名不能为空" 
    data = models.Asset.objects.all()
    ret['data'] = data    
    return render(request,"web/host_del.html",ret)

@outer
def host_mod(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    if request.method == 'POST':
        selectval = request.POST.get('selectval',None)
        ip = request.POST.get('ip',None)
        infonew = request.POST.get('infonew',None)
        is_empty = all([selectval,infonew,ip])
        if is_empty:
            count = models.Asset.objects.filter(ip=ip).count()
            if count==0:
                ret['status'] = "主机不存在"
            else:
                if str(selectval) == 'Ip':  
                    models.Asset.objects.filter(ip=ip).update(ip=infonew)
                    ret['status']="用户密码修改成功"
                else:
                    models.Asset.objects.filter(ip=ip).update(hostname=infonew)
                    ret['status']="用户邮箱修改成功"
                return redirect("/web/host_mod.html")
        else:
            ret['status'] = "用户修改信息不能为空"  
    return render(request,"web/host_mod.html",ret)


@outer
def type_add(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    if request.method == 'POST':
        typename = request.POST.get('typename',None)
        is_empty = all([typename])
        if is_empty:
            count = models.UserType.objects.filter(typename=typename).count()
            if count==1:
                ret['status'] = "Usertype已存在"
            else:    
                models.UserType.objects.create(typename=typename)
                ret['status']="用户类型添加成功"
                return redirect("/web/type_add.html")
        else:
            ret['status'] = "Usertype不能为空" 
    data = models.UserType.objects.all()
    ret['data'] = data    
    return render(request,"web/type_add.html",ret)

@outer
def type_del(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    if request.method == 'POST':
        typename = request.POST.get('typename',None)
        is_empty = all([typename])
        if is_empty:
            count = models.UserType.objects.filter(typename=typename).count()
            if count==0:
                ret['status'] = "Usertype不存在"
            else:    
                models.UserType.objects.get(typename=typename).delete()
                ret['status']="用户类型删除成功"
                return redirect("/web/type_del.html")
        else:
            ret['status'] = "Usertype不能为空" 
    data = models.UserType.objects.all()
    ret['data'] = data    
    return render(request,"web/type_del.html",ret)

@outer
def type_mod(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    if request.method == 'POST':
        typenameold = request.POST.get('typenameold',None)
        typenamenew = request.POST.get('typenamenew',None)
        is_empty = all([typenameold,typenamenew])
        if is_empty:
            count = models.UserType.objects.filter(typename=typenameold).count()
            if count==0:
                ret['status'] = "Usertype不存在"
            else:    
                models.UserType.objects.filter(typename=typenameold).update(typename=typenamenew)
                ret['status']="用户类型修改成功"
                return redirect("/web/type_mod.html")
        else:
            ret['status'] = "Usertype不能为空" 
    data = models.UserType.objects.all()
    ret['data'] = data    
    return render(request,"web/type_mod.html",ret)

@outer
def type_get(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    data = models.UserType.objects.all()
    ret['data'] = data    
    return render(request,"web/type_get.html",ret)

@outer
def user_add(request):
    ret = {'status':'','usertype':None}
    usertype = models.UserType.objects.all()
    ret['usertype'] = usertype
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        email = request.POST.get('email',None)
        usertype_id = request.POST.get('usertype',None)
        is_empty = all([username,password,email])
        if is_empty:
            usertypeobj = models.UserType.objects.get(id=usertype_id)
            models.UserInfo.objects.create(username=username,
                                        password=password,
                                        email=email,
                                        user_type=usertypeobj)
            ret['status']="注册成功"
            return redirect("/web/user_add.html")
        else:
            ret['status'] = "Username、Password、Email不能为空"     
    return render(request,"web/user_add.html",ret)

@outer
def user_get(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    data = models.UserInfo.objects.filter(username=user_dict['user'])
    ret['data'] = data    
    return render(request,"web/user_get.html",ret)

@outer
def user_mod(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    if request.method == 'POST':
        selectval = request.POST.get('selectval',None)
        password = request.POST.get('password',None)
        infonew = request.POST.get('infonew',None)
        is_empty = all([infonew,password])
        if is_empty:
            count = models.UserInfo.objects.filter(username=user_dict['user'],password=password).count()
            if count==0:
                ret['status'] = "用户名密码不对，请重新输入"
            else:
                if str(selectval) == 'password':  
                    models.UserInfo.objects.filter(username=user_dict['user'],password=password).update(password=infonew)
                    ret['status']="用户密码修改成功"
                else:
                    models.UserInfo.objects.filter(username=user_dict['user'],password=password).update(email=infonew)
                    ret['status']="用户邮箱修改成功"
                #return redirect("/web/user_mod.html")
        else:
            ret['status'] = "用户修改信息不能为空"  
    return render(request,"web/user_mod.html",ret)


def user_del(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    if request.method == 'POST':
        username = request.POST.get('username',None)
        is_empty = all([username])
        if is_empty:
            count = models.UserInfo.objects.filter(username=username).count()
            if count==0:
                ret['status'] = "用户名不存在"
            else:    
                models.UserInfo.objects.get(username=username).delete()
                ret['status']="用户名删除成功"
                return redirect("/web/user_del.html")
        else:
            ret['status'] = "用户名不能为空"  
    return render(request,"web/user_del.html",ret)


@outer
def group_add(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    if request.method == 'POST':
        groupname = request.POST.get('groupname',None)
        is_empty = all([groupname])
        if is_empty:
            count = models.UserGroup.objects.filter(grouname=groupname).count()
            if count==1:
                ret['status'] = "用户组已存在"
            else:    
                models.UserGroup.objects.create(grouname=groupname)
                ret['status']="用户组添加成功"
                return redirect("/web/group_add.html")
        else:
            ret['status'] = "用户组不能为空"
    return render(request,"web/group_add.html",ret)

@outer
def group_get(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    data = models.UserGroup.objects.all()
    ret['data'] = data    
    return render(request,"web/group_get.html",ret)


@outer
def group_del(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    if request.method == 'POST':
        groupname = request.POST.get('groupname',None)
        is_empty = all([groupname])
        if is_empty:
            count = models.UserGroup.objects.filter(groupname=groupname).count()
            if count==0:
                ret['status'] = "用户组不存在"
            else:    
                models.UserGroup.objects.get(groupname=groupname).delete()
                ret['status']="用户组删除成功"
                return redirect("/web/group_del.html")
        else:
            ret['status'] = "用户组名不能为空" 
    data = models.UserGroup.objects.all()
    ret['data'] = data    
    return render(request,"web/group_del.html",ret)

@outer
def group_mod(request):
    user_dict = request.session.get('is_login',None)
    ret = {'status':'','data':'','username':user_dict['user']}
    if request.method == 'POST':
        groupnameold = request.POST.get('groupnameold',None)
        groupnamenew = request.POST.get('groupnamenew',None)
        is_empty = all([groupnameold,groupnamenew])
        if is_empty:
            count = models.UserGroup.objects.filter(groupname=groupnameold).count()
            if count==0:
                ret['status'] = "用户组不存在"
            else:    
                models.UserGroup.objects.filter(groupname=groupnameold).update(groupname=groupnamenew)
                ret['status']="用户组修改成功"
                return redirect("/web/group_mod.html")
        else:
            ret['status'] = "用户组名不能为空" 
    data = models.UserGroup.objects.all()
    ret['data'] = data    
    return render(request,"web/group_mod.html",ret)

