#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-8 @Author:Guolikai'''

class MyException(Exception):
    def __init__(self,msg):
        self.error = msg
    def __str__(self,*args,**kwargs):
        return  self.error                  #结果直接返给对象

obj = MyException('出现错误')
print obj