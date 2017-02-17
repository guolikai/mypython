#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2017-2-10 @Author:Guolikai'''

from django.contrib import admin
import models
# Register your models here.
class BBS_admin(admin.ModelAdmin):
    list_display=('title','summary','user','email','favor_count','reply_count','create_date')
    list_filter=('create_date',)
    search_fields =('title','user__username')
    #用于关联另一张表的字段信息
    def email(self,obj):    
        return obj.user.email
    #修改要显示的名称
    email.short_description = '邮箱'
admin.site.register(models.News,BBS_admin)
admin.site.register(models.User)
admin.site.register(models.UserType)
admin.site.register(models.Chat)
admin.site.register(models.NewsType)
admin.site.register(models.Reply)