#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import sys
sys.path.append('/root/python/day08/Monitor')
class BaseService(object):
    def __init__(self):
        self.name  = 'BaseService'
        self.interval = 300
        self.last_time = 0
        self.plugin_name = 'your_plugin_name'
        self.triggers = {}