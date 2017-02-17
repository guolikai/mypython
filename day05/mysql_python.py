#!/usr/bin/env python
#coding:utf8
#http://www.cnblogs.com/wupeiqi/articles/4198124.html
import MySQLdb
'''
#连接数据库
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='mysql',port=3306)
#数据中的光标(指针)
cur = conn.cursor()
#返回此次查询影响到的数据条目
reCount = cur.execute('select user,host from mysql.user')
#获取查询到的数据
data = cur.fetchall()
#关闭指针
cur.close()
#关闭连接
conn.close()

print reCount
print data'''
'''
#创建数据库
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='mysql',port=3306)
cur = conn.cursor()
cur.execute("""create database if not exists bankdata""")
conn.select_db('bankdata');
cur.execute("""create table userinfo(id int(2) primary key auto_increment, name varchar(10),passwd varchar(10),money int(2),credit_money int(2))""")
conn.commit()   #提交本次请求
cur.close()
#插入数据
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='bankdata',port=3306)
cur = conn.cursor()
sql = "insert into userinfo (name,passwd,money,credit_money) values(%s,%s,%s,%s)"
karges = ('user10','123456',20000,0)
reCount = cur.execute(sql,karges)
conn.commit()   #提交本次请求
cur.close()
conn.close()
#删除数据
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='bankdata',port=3306)
cur = conn.cursor()
sql = "delete from userinfo where name=%s"
karges = ('user05',)
reCount = cur.execute(sql,karges)
conn.commit()   #提交本次请求
cur.close()
conn.close()
print reCount
#跟新数据
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='bankdata',port=3306)
cur = conn.cursor()
sql = "update userinfo set passwd=%s where name=%s"
karges = ('123456','user07')
reCount = cur.execute(sql,karges)
conn.commit()   #提交本次请求
cur.close()
conn.close()
print reCount
'''
#插入多条数据
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='bankdata',port=3306)
cur = conn.cursor()
sql = "insert into userinfo (name,passwd,money,credit_money) values(%s,%s,%s,%s)"
karges = [('user05','123456',20000,0),('user08','123456',20000,0)]
reCount = cur.executemany(sql,karges)
conn.commit()   #提交本次请求
cur.close()
conn.close()
