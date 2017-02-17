#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-8 @Author:Guolikai'''

#抽象类+抽象方法 == 接口
from abc import ABCMeta,abstractmethod
class jiekou:
    __metaclass__ = ABCMeta
    @abstractmethod
    def send(self):
        pass
class Foo(jiekou):
    def __init__(self):
        print '__init__'
    def send(self):
        print 'send.微信代码'
f = Foo()
f.send()
