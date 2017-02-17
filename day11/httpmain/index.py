#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
from wsgiref.simple_server import make_server
import conf
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 获取用户的URL
    userUrl = environ['PATH_INFO']
    for item in conf.url:
        if item[0]==userUrl:
            return item[1]()
        #else:
            #return '<h1>404 Not Found</h1>'
    '''
    if userUrl=='/index/':
        return '<h1>Hello, web!</h1>'
    elif userUrl=='/login/':
        return '<h1>Login</h1>'
    elif userUrl == '/logout/':
        return '<h1>Logout</h1>'
    else:
        return '<h1>404 Not Found!</h1>'
    '''
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()