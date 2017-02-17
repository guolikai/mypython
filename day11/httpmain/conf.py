#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
def index():
    return  'index'
def login():
    html1='<p>用户名<input type="text"/></p><p>密码<input type="text"/></p>'
    return html1
def logout():
    return  'logout'

url = (
    ('/index',index),
    ('/manager',login),
    ('/login',login),
    ('/login/',login),
    ('/logout',logout),
)
