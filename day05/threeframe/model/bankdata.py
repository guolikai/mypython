#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
from utility.sql_helper import MysqlHelper
class UserInfo(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def GetOne(self,username,password):
        sql = 'select * from bankdata.userinfo where user=%s and password=%s'
        params = (username,password,)
        return self.__helper.GetOne(sql,params)
    def GetDict(self,username,password):
        sql = 'select * from bankdata.userinfo where user=%s and password=%s'
        params = (username,password)
        return self.__helper.GetDict(sql,params)