#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-5
@Author:Guolikai'''
def glkreadlines():
    seek = 0
    while True:
        with open('E:/temp.txt','r')  as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return
for item in glkreadlines():
    print item