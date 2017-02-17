#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-5 @Author:Guolikai'''
from  multiprocessing import Pool
import time
def Foo(n):
    time.sleep(1)
    print n*n
    return n*n
if __name__ == '__main__':
    p = Pool(50)
    print p.map(Foo,range(100))