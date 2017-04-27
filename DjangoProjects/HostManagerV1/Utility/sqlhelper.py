#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-1 @Author:Guolikai'''
import sys
import globalsetting
import MySQLdb
import conf
class MysqlHelper(object):
    def __init__(self):
        self.__conn_dict = conf.conn_dict

    def SelectDict(self,sql,params):
        #conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', port=3306)
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        reCount = cur.execute(sql,params)
        data = cur.fetchall()
        cur.close()
        conn.close()             
        return  data

    def SelectOne(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor()
        reCount = cur.execute(sql,params)
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data

    def Insert(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor()
        reCount = cur.execute(sql,params)
        conn.commit()
        return reCount
        cur.close()
        conn.close()

    def Delete(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor()
        reCount = cur.execute(sql,params)
        conn.commit()
        return reCount
        cur.close()
        conn.close()

    def Update(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor()
        reCount = cur.execute(sql,params)
        conn.commit()
        return reCount
        cur.close()
        conn.close()
