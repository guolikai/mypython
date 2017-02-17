#!/usr/bin/env python
#coding:utf8
'''Created on 2016-11-26 @Author:Guolikai'''
import socket,os,time
Host = '127.0.0.1'
Port = 9000
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((Host,Port))
def recv_all(obj,msg_length):
	raw_result = 0
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
	user_input = raw_input("Message to sed[put /etc/passwd]:").strip()
	if len(user_input) == 0:
		continue
	cmd,path = user_input.split()
	print cmd,path
	if cmd == 'put':
		f = file(path,'rb')	
		file_name = os.path.basename(path)
		file_size = os.stat(path).st_size
		c.send("%s %s %s" % (cmd,file_name,file_size))
		print 'Going to send...'
		time.sleep(10)
		c.sendall(f.read())
		print c.recv(1024)
		f.close()
c.close()
