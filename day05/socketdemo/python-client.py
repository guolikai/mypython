#!/usr/bin/python
#coding:utf8
import socket
Host = '192.168.4.100'
Port = 9000
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((Host,Port))
while True:
	user_input = raw_input("message to sed::").strip()
	c.send(user_input)
	return_data = c.recv(1024)
	print 'Recved:',return_data
c.close()