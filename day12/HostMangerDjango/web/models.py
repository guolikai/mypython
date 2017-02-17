#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-20 @Author:Guolikai'''

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserType(models.Model):
    typename = models.CharField(max_length=50)
    
class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email  = models.EmailField()
    user_type = models.ForeignKey("UserType")    

class UserGroup(models.Model):
    groupname = models.CharField(max_length=50)
    user = models.ManyToManyField("UserInfo")
    
class Asset(models.Model):
    hostname = models.CharField(max_length=256)
    ip =models.GenericIPAddressField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user_group = models.ForeignKey("UserGroup")
    def __unicode__(self):
        temp = "Current Object Asset(include:%s %s)" % (self.hostname,self.ip)
        return temp
    