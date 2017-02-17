#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-5 @Author:Guolikai'''
from  multiprocessing import Pool
import time
def run(x):
    print x*x
    time.sleep(1)
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=5)
    res_list = []
    for i in range(10):
        res = pool.apply_async(run,(i,))
        print '______________',i
        res_list.append(res)
    #print pool.map(run,range(10))
    #print res_list
    for r in res_list:
        print r.get()
        #print r.get(timeout=1)
