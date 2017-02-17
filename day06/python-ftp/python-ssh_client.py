#!/usr/bin/env python
#coding:utf8
'''Created on 2016-11-26 @Author:Guolikai'''
import socket
Host = '172.16.1.100'
Port = 9000
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((Host,Port))

def recv_all(obj,msg_length):
	raw_result = ''
	while msg_length !=0:
		if msg_length <= 4096:
			data= obj.recv(msg_length)
			msg_length = 0
		else:
			data= obj.recv(4096)
			msg_length -= 4096
		raw_result += data
	return raw_result

while True:
	user_input = raw_input("Message to sed::").strip()
	if len(user_input) == 0:
	    continue
	c.send(user_input)
	#recy response size
	res_size = int(c.recv(1024) )
	print 'Received size   form server\n',res_size
	#return_data = c.recv(1024)
	input_result  = recv_all(c,res_size)
	print 'Received result from server:\n',input_result
c.close()
