#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-5 @Author:Guolikai'''
'''进程间内存共享'''
from multiprocessing import Process,Array,Value
from  threading import Thread
def run(n,a):
    n.value=3.1415926
    for i in range(5):
        a[i]=-a[i]

if __name__ == '__main__':
    num = Value('d',0.0)
    arr = Array('i',range(20))
    p = Process(target=run,args=(num,arr))
    #p = Thread(target=run,args=(num,arr))
    p.start()
    print num.value
    print arr[:]
    p.join()
    print num.value
    print arr[:]