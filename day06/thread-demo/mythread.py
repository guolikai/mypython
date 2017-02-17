#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-26 @Author:Guolikai'''
from threading import  Thread
import time
'''
class Mythread(Thread):
    def run(self):
        time.sleep(5)
        print "我是子线程"

def func2(aggs):
    print 'func2'* aggs

t1 = Mythread(target=func2,args=(4,))
#会执行从Thread继承来的构造函数（__init__）,但是func2未执行
t1.start()
print 'over'
'''
class Mythread(Thread):
    def run(self):
        time.sleep(5)
        print "我是子线程"
        Thread.run(self)
def func2(aggs):
    print 'func2'* aggs,

t1 = Mythread(target=func2,args=(3,))
#会执行从Thread继承来的构造函数（__init__）,但是func2未执行
t1.start()
print 'over'