#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-26 @Author:Guolikai'''
import threading
import time
'''
lock = threading.Lock()
num = 0
def run():
    time.sleep(0.1)
    global num
    lock.acquire()
    num += 1
    lock.release()
    #time.sleep(0.01)
    print '%s\n' % num
for i in range(100):
    t = threading.Thread(target=run,args=())
    t.start()
'''
'''
lock = threading.RLock()
num = 0
num2 = 0
def run():
    time.sleep(0.1)
    global num
    global num2
    lock.acquire()
    num += 1
    lock.release()
    lock.acquire()
    num2 += 2
    lock.release()
    #time.sleep(0.01)
    print '%s %s\n' % (num,num2)
for i in range(100):
    t = threading.Thread(target=run,args=())
    t.start()
'''
samp = threading.BoundedSemaphore(4)
num = 0
def run():
    time.sleep(1)
    global num
    samp.acquire()
    num += 1
    samp.release()
    #time.sleep(0.01)
    print '%s\n' % num
for i in range(100):
    t = threading.Thread(target=run,args=())
    t.start()