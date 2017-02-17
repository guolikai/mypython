#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-16 @Author:Guolikai'''
from wsgiref.simple_server import make_server
from Controller.Account import *
from Controller.Admin import *
url = (
    ('/index',index),
    ('/manager',login),
    ('/login',login),
    ('/login/',login),
    ('/logout',logout),
)
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 获取用户的URL
    userUrl = environ['PATH_INFO']
    for item in url:
        if item[0]==userUrl:
            return item[1]()
        #else:
           #return '<h1>404 Not Found</h1>'
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()