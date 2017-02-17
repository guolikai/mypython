#!/usr/bin/env python
#coding:utf8
'''Created on 2016-11-26 @Author:Guolikai'''
import SocketServer
import time,commands
class MySockServer(SocketServer.BaseRequestHandler):
    def handle(self):
        print 'Got a new connection from',self.client_address
	while True:
	    cmd = self.request.recv(1024)
	    if not cmd:
		print 'Lost connection with',self.client_address
		break
	    cmd_result = commands.getstatusoutput(cmd)
	    self.request.send( str( len(cmd_result[1]) ) )
	    time.sleep(0.1)
	    self.request.send(cmd_result[1])

if __name__ ==  '__main__':
    h = '0.0.0.0'
    p = 9000
    s = SocketServer.ThreadingTCPServer((h,p),MySockServer)
    s.serve_forever()
    
