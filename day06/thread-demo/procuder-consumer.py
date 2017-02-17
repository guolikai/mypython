#!/usr/bin/env python
# _*_ coding:utf8 _*_
import threading
import Queue
import time
import random
def Proudcer(name,que):
    while True:
        if que.qsize() <5:
            que.put('包子')
            print '%s:生产了一个包子==========='  % name
        else:
            print '还有5个包子'
        time.sleep(random.randrange(2))

def Consumer(name,que):
    while True:
        try:
            que.get_nowait()
            print '%s:吃了一个包子' % name
        except Exception:
            print '没有包子'
        time.sleep(random.randrange(3))
q = Queue.Queue()
p1 = threading.Thread(target=Proudcer,args=('glk',q))
p2 = threading.Thread(target=Proudcer,args=('wdx',q))
p1.start()
p2.start()

c1 = threading.Thread(target=Consumer,args=('c1',q))
c2 = threading.Thread(target=Consumer,args=('c2',q))
c1.start()
c2.start()