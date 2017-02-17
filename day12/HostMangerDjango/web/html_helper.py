#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-22 @Author:Guolikai'''
from django.utils.safestring import mark_safe


class PageInfo(object):
    def __init__(self,current_page,all_count,per_item=5):
        self.CurrentPage =  current_page
        self.AllCount =  all_count
        self.PerItem =  per_item
        
    '''
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
    '''
    @property
    def start(self):
        return (self.CurrentPage-1)*self.PerItem
    
    @property
    def end(self):
        return (self.CurrentPage) * self.PerItem 
    
    @property
    def pages_all_count(self):
        temp = divmod(self.AllCount,self.PerItem)
        if temp[1]==0:
            pages_all_count = temp[0]
        else:
            pages_all_count = temp[0] + 1
        
        return  pages_all_count


def Pager(page,pages_all_count):
    '''page:当前页；pages_all_count：总页数'''
    page_html = []  
    first_html = "<a href='/web/host_list.html/%d'>首页 </a>" % (1) 
    page_html.append(first_html)
    if page <=1:
        prev_html = "<a href='#'>上一页 </a>"
    else:    
        prev_html = "<a href='/web/host_list.html/%d'>上一页 </a>" % (page-1) 
    page_html.append(prev_html)
    for i in range(pages_all_count):
        if page == i+1:
            a_html = "<a class='selected' href='/web/host_list.html/%d'>%d </a>" % (i+1,i+1)
        else:
            a_html = "<a href='/web/host_list.html/%d'>%d </a>" % (i+1,i+1)
        page_html.append(a_html)
        
    if page+1 > pages_all_count:
        next_html =  "<a href='#'>下一页 </a>"
    else:     
        next_html = "<a href='/web/host_list.html/%d'>下一页 </a>" % (page+1) 
    page_html.append(next_html)
       
    end_html =  "<a href='/web/host_list.html/%d'>尾页 </a>" % (pages_all_count) 
    page_html.append(end_html)    
        
    page_string = mark_safe(''.join(page_html))
    
    return page_string