#!/usr/bin/pythin
#coding:utf8
import socket
Host,Port = '0.0.0.0',9000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,Port))
s.listen(1)
conn,addr = s.accept()

while True:
	print 'Got a connection from',addr
	data = conn.recv(1024)
	if not data:break
	conn.send(data.upper())
	print 'Received ..:' ,data
s.close()
