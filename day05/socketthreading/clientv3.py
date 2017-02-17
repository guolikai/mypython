#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
import socket
client = socket.socket()
ip_port = ('127.0.0.1',8090)
client.connect(ip_port)
while True:
	data = client.recv(1024)
	print data
	inp = raw_input('CLient:')
	client.send(inp)
        if inp == 'exit':
	    break
