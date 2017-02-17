#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-16 @Author:Guolikai'''
import Globalsetting
def login():
    #获取
    #数据库比较用户名密码
    #Model成功跳转，不成功返回View
    f = file('E:\python08\day11\PythonWeb\View\usermima.html','r')
    data = f.read()
    return data
def logout():
    return  'logout'