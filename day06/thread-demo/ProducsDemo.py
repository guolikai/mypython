#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-26 @Author:Guolikai'''
from threading import Thread
from Queue import Queue
import time
class Procuder(Thread):
    def __init__(self,name,queue):
        #生产者的名字name；queue容器池子
        self.__Name = name
        self.__Queue = queue
        super(Procuder,self).__init__()   #执行父类的构造函数
    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(1)
            else:
                self.__Queue.put('包子')
                time.sleep(1)
                print '%s生产了一个包子 ' % (self.__Name,)
        Thread.run(self)

class Consumer(Thread):
    def __init__(self, name, queue):
        # 生产者的名字name；queue容器池子
        self.__Name = name
        self.__Queue = queue
        super(Consumer, self).__init__()
    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(1)
            else:
                self.__Queue.get('包子')
                time.sleep(1)
                print '%s消费了一个包子 ' % (self.__Name,)
        Thread.run(self)

queue = Queue(maxsize=100)  #申明队列，先进先出，线程安全区,
glk1 = Procuder('glk1',queue)
glk1.start()
glk2 = Procuder('glk2',queue)
glk2.start()
glk3 = Procuder('glk3',queue)
glk3.start()

for item in range(20):
    name = 'wdx%d' % (item,)
    temp = Consumer(name,queue)
    temp.start()
'''
print 'empty:',queue.empty()
print queue.qsize()  #查看队列中的数据
queue.put('1')
queue.put('2')
print queue.qsize()
print 'get:',queue.get()
print queue.qsize()
print 'empty:',queue.empty()
print 'get:',queue.get()
print queue.qsize()
print 'get:',queue.get()
'''