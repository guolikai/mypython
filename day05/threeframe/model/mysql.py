#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
from utility.sql_helper import MysqlHelper
class user(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def get_one(self,user):
        sql = 'select * from mysql.user where user=%s'
        params = ('root',)
        return self.__helper.Get_one(sql,params)