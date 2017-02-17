#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-17 @Author:Guolikai'''
import MySQLdb
import conf
class MysqlHelper(object):
    def __init__(self):
        self.__conn_dict = conf.conn_dict
    def GetDict(self,sql,params):
        #conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', port=3306)
        conn = MySQLdb.connect(**self.__conn_dict)  #连接数据库，**表示传递的数据是字典类型
        # cur = conn.cursor()  # 数据中的光标(指针),返回的数据是元组类型
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)   # 数据中的光标(指针),返回的数据是字典类型
        reCount = cur.execute(sql,params)   # 返回此次查询影响到的数据条目
        data = cur.fetchall()    # 获取查询到的所有数据
        cur.close()              # 关闭指针
        conn.close()             # 关闭连接
        return  data
    def GetOne(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        reCount = cur.execute(sql, params)
        data = cur.fetone()
        cur.close()
        conn.close()
        return data