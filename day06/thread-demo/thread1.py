#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-26 @Author:Guolikai'''
from threading import Thread
import time
def Foo(arg):
    print arg,
t1 = Thread(target=Foo,args=(1,))
t1.start()

def Fun1(arg):
    for item in range(20):
        print item,
        time.sleep(1)
print "before"
t2 = Thread(target=Fun1,args=(1,))
t2.setDaemon(True)
print t2.getName()
t2.start()
t2.join(10)
time.sleep(5)
print "after"
print "after"
print "after end"