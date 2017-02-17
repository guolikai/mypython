#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-20 @Author:Guolikai'''

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=256)
    ip = models.GenericIPAddressField()