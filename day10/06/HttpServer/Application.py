#!/usr/bin/env python

def RunServer(environ, start_response):
	#start_response('200 OK', [('Content-Type', 'text/html')])
	#return '<h1>Hello, web!</h1>'
	
	start_response('200 OK', [('Content-Type', 'text/json')])
	return "{name:'hanxin',age:18}"