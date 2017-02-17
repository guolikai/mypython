#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-5 @Author:Guolikai'''
'''进程与进程之间共享multiprocessing.Queue'''
from multiprocessing import  Process,Queue
def run(q,n):
    q.put([n,'hello'])

if __name__ == '__main__':
    q = Queue()
    for i in range(10):
        p = Process(target=run,args=(q,i))
        p.start()
    while True:
        print q.get()
