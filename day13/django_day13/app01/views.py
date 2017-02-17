#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-22 @Author:Guolikai'''

from django.shortcuts import render,render_to_response
from app01 import models
from app01 import common
from django.core.paginator import Page
from django.utils.safestring import mark_safe
from app01 import html_helper
# Create your views here.
def  index(request,page):
    per_item = common.try_int(request.COOKIES.get('pager_num',10),10)
    #操作数据库进行分页
    page = common.try_int(page,1)
    count = models.Host.objects.all().count()
    pageobj =  html_helper.PageInfo(page,count,per_item)
    result = models.Host.objects.all()[pageobj.start:pageobj.end]
    page_string = html_helper.Pager(page,pageobj.pages_all_count)
    ret = {'data':result,'count':count,'page':page_string}
    response = render_to_response('app01/index.html',ret)
    response.set_cookie('pager_num',per_item)
    return response