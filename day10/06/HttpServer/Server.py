#!/usr/bin/env python
#coding:utf-8

from wsgiref.simple_server import make_server
import Application

httpd = make_server('', 8000, Application.RunServer)
print "Serving HTTP on port 8000..."
httpd.serve_forever()
