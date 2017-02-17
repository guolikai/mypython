#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-5 @Author:Guolikai'''
from  multiprocessing import Process
import os
def info(title):
    print title
    print 'module name',__name__
    if hasattr(os,'getppid'):
        print 'parent prcocess',os.getppid()
    print 'process id',os.getpid()

def f(name):
    info('function f')
    print 'Hello',name

if __name__ == '__main__':
    info('main line')
    print '_________________________'
    p = Process(target=f,args=('glk',))
    p.start()
    p.join()