#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-8 @Author:Guolikai'''
#经典类与新式类区别https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html
#class A(object):             #新式类
class A:                      #经典类
    def __init__(self):
        print 'This is A'
    def save(self):
        print 'The method from A'

class B(A):
    def __init__(self):
        print 'This is B'

class C(A):
    def __init__(self):
        print 'This is C'
    def save(self):
        print 'The method from --C--'

class D(B,C):
    def __init__(self):
        print 'This is D'

D1 = D()
D1.save()