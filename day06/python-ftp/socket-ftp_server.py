#!/usr/bin/env python
#coding:utf8
'''Created on 2016-11-26 @Author:Guolikai'''
import SocketServer
import time,commands
def recv_all(obj,msg_length,des_file):
	while msg_length !=0:
		if msg_length <= 4096:
			print "deff",msg_length
			data= obj.recv(msg_length)
			msg_length = 0
		else:
			data= obj.recv(4096)
			msg_length -= 4096
			print msg_length
		des_file.write(data)
		return  'Done'

class MySockServer(SocketServer.BaseRequestHandler):
	def handle(self):
		print 'Got a new connection from',self.client_address
		while True:
			cmd = self.request.recv(1024)
			print cmd
			option,filename,file_size = cmd.split()
			print option,filename,file_size
			if option == 'put':
				#client wants to upload file
				f = file('/tmp/%s' % filename,'wb') #wb二进制文件
				write_to_file = recv_all(self.request,int(file_size),f)
				if write_to_file == 'Done':
					self.request.send('File uploaded success!\n')
					f.close()
if __name__ ==  '__main__':
	h = '0.0.0.0'
	p = 9000
	s = SocketServer.ThreadingTCPServer((h,p),MySockServer)
	s.serve_forever()
    
