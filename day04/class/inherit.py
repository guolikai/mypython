#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-8 @Author:Guolikai'''
class Father:
    def __init__(self):
        self.Fname = 'FFFFF'
    def func(self):
        print 'father.func'
    def bad(self):
        print 'bad 习惯'

class Son(Father):
    def __init__(self):
        self.Sname = 'SSSSS'
    def Bar(self):
        print 'son.func'
    '''
    def bad(self):                      #对父类(基类)的bad方法进行了重写
        print 'bad习惯'
    '''
    def bad(self):
        Father.bad(self)
        print '+++bad习惯'
s1 = Son()
s1.Bar()
s1.func()
s1.bad()