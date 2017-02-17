#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
import socket
sk = socket.socket()
ip_port = ('127.0.0.1',8090)
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,address = sk.accept()
    conn.send('hello,you good!',)
    conn.close()