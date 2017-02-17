#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import sys
sys.path.append('/root/python/day08/Monitor/conf')
from Service import Linux

class BaseTemplate(object):
    def __init__(self):
        self.name = 'YourTemplateName'
        self.groupname = 'YourGroupName'
        self.hosts = []
        self.services = []

class LinuxTemplate(BaseTemplate):
    def __init__(self):
        super(LinuxTemplate,self).__init__()
        self.name = 'LinuxTemplate'
        self.services = [
            Linux.CPU,
            Linux.Memory
            ]

if __name__ == '__main__':
    t = LinuxTemplate()
    t.hosts = ['172.16.1.100','172.16.1.110','172.16.1.120']

    for service in t.services:
        service =  service()
        if service.name=='linux_cpu':
            service.interval = 90
        print service.name,service.interval