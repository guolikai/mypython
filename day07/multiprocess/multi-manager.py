#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-5 @Author:Guolikai'''
from multiprocessing import Manager,Process
def run(d,l):
    d[1]='1'
    d['2']=2
    d[0.25]=None
    l.reverse()   #列表反转

if __name__ == '__main__':
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))
    p = Process(target=run,args=(d,l))
    p.start()
    p.join()
    print d
    print l