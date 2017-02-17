#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-5 @Author:Guolikai'''
from multiprocessing import Process
from threading import Thread
import os
def fun(li,n):
    print 'Thread:%s ---> %s' % (os.getpid(),n)

def run(info_list,n):
    info_list.append(n)
    #print info_list
    for i in range(5):
        p = Thread(target=fun,args=(info_list,i))
        p.start()

if __name__ == '__main__':
    info = []
    for i  in range(10):
        p = Process(target=run,args=[info,i])
        p.start()
