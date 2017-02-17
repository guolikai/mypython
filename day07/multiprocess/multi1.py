#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-5 @Author:Guolikai'''
from multiprocessing import Process
from threading import Thread
def run(info_list,n):
    info_list.append(n)
    print info_list

if __name__ == '__main__':
    info = []
    for i  in range(10):
        p = Process(target=run,args=[info,i])
        p.start()
    print "_______________________________________"
    for i  in range(10):
        p = Thread(target=run,args=[info,i])
        p.start()