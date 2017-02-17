#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-5 @Author:Guolikai'''
'''进程同步'''
from multiprocessing import Process,Lock
def run(l,num):
    l.acquire()
    print 'hello word',num
    l.release()

if __name__ == '__main__':
    lock = Lock()
    for num in range(50):
        p = Process(target=run,args=(lock,num))
        p.start()
        p.join()