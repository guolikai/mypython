#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-22 @Author:Guolikai'''

from django.shortcuts import render,render_to_response
from app01 import models
from app01 import common
from django.core.paginator import Page
from django.utils.safestring import mark_safe
# Create your views here.
def  index(request,page):
    #操作数据库进行分页
    page = common.try_int(page,1)
    per_item = 2
    start = (page-1)*per_item
    end = page*per_item
    count = models.Host.objects.all().count()
    result = models.Host.objects.all()[start:end]
    temp = divmod(count,per_item)
    if temp[1]==0:
        pages_all_count = temp[0]
    else:
        pages_all_count = temp[0] + 1
    page_html = []  
    
    first_html = "<a href='/index/%d'>首页 </a>" % (1) 
    page_html.append(first_html)
    if page <=1:
        prev_html = "<a href='#'>上一页 </a>"
    else:    
        prev_html = "<a href='/index/%d'>上一页 </a>" % (page-1) 
    page_html.append(prev_html)
    for i in range(pages_all_count):
        if page == i+1:
            a_html = "<a class='selected' href='/index/%d'>%d </a>" % (i+1,i+1)
        else:
            a_html = "<a href='/index/%d'>%d </a>" % (i+1,i+1)
        page_html.append(a_html)
        
    if page+1 > pages_all_count:
        next_html =  "<a href='#'>下一页 </a>"
    else:     
        next_html = "<a href='/index/%d'>下一页 </a>" % (page+1) 
    page_html.append(next_html)
       
    end_html =  "<a href='/index/%d'>尾页 </a>" % (pages_all_count) 
    page_html.append(end_html)    
        
    page_all = mark_safe(''.join(page_html))
    ret = {'data':result,'count':count,'page':page_all}
    print result
    return render_to_response('index.html',ret)