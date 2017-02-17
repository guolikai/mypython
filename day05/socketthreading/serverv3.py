#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
#实现异步多线程服务端
import SocketServer
class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass
    def handle(self):
        #print self.request self.client_address self.server
        conn = self.request
        conn.send('hello,you good!',)
        flag = True
        while flag:
            data = conn.recv(1024)
            print data
            if data == 'exit':
                flag = False
            conn.send('sb',)
        conn.close()
    def finish(self):
        pass
if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',8090),MyServer)
    server.serve_forever()