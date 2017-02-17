#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import sys
sys.path.append('/root/python/day08/Monitor/conf')
import Templates

g1 = Templates.LinuxTemplate()
g1.groupname = 'muban_group'
g1.hosts = ['172.16.1.110','172.16.1.120']

g2 = Templates.LinuxTemplate()
g2.groupname = 'kvm_group'
g2.hosts = ['172.16.1.101']

monitored_groups = [g1,g2]