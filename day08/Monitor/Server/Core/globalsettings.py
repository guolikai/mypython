#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import os,sys
#sys.path.append('/root/python/day08/Monitor/conf')
base_dir = os.path.dirname(os.path.dirname(__file__))
#base_dir py文件目录的上一层目录
print base_dir
sys.path.append(base_dir)