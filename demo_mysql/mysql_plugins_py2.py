#/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import os
import commands
import datetime
import MySQLdb
import time
import weekmonth
import json
import database

def get_data( sql,database ):
	conn_in=MySQLdb.connect(host="192.168.30.191",user="root",passwd="srtroot",db=database,charset="utf8")
	cursor_in = conn_in.cursor()
	cursor_in.execute( sql)
	rows    =   cursor_in.fetchall()
	cursor_in.close()
	conn_in.close()
	return rows
  
def exec_sql(sql, database):
	conn_in=MySQLdb.connect(host="192.168.30.191",user="root",passwd="srtroot",db=database,charset="utf8")
	cursor_in = conn_in.cursor()
	cursor_in.execute( sql)
	conn_in.commit()
	cursor_in.close()
	conn_in.close()
  
def get_yesterday( today, days):
	oneday = datetime.timedelta(days) 
	yesterday = today - oneday
	return yesterday
	print yesterday,type(yesterday)
