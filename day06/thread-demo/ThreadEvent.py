#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-26 @Author:Guolikai'''

import threading
import time
event = threading.Event()
'''
def Proudcer():
    print '厨师：等人来买包子...'
    event.wait()
    event.clear()
    print '厨师：正在做包子'
    time.sleep(5)
    print '厨师：包子做好了'
    event.set()
def Consumer():
    print '顾客：来买包子...'
    event.set()
    print '顾客：正在等厨师做好包子...'
    time.sleep(2)
    event.wait()
    print '顾客：包子真好吃...'

p = threading.Thread(target=Proudcer)
c = threading.Thread(target=Consumer)
p.start()
c.start()
'''
def Proudcer():
    print '厨师：等人来买包子...'
    event.wait()
    event.clear()
    print '厨师：正在做包子'
    time.sleep(3)
    print '厨师：包子做好了'
    event.set()
def Consumer():
    print '顾客：来买包子...'
    event.set()
    print '顾客：正在等厨师做好包子...'
    time.sleep(2)
    while True:
        if event.is_set():
            print '顾客：包子真好吃...'
            break
        else:
            print '顾客：包子换没好，厨师真慢...'
        time.sleep(0.2)
p = threading.Thread(target=Proudcer)
c = threading.Thread(target=Consumer)
p.start()
c.start()