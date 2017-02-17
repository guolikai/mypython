#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-5
@Author:Guolikai'''
def outer(fun):    #定义装饰器wrapper
    def wrapper(arg):
        print '验证代码'
        result = fun(arg)
        return result
    return  wrapper
@outer    #装饰器与函数发生关系@outer=outer(Func1)
def Func1(arg):
    print 'func1',arg
    return 'return'
#下面有10000个函数
#产品经理提出需求，每个函数执行前加一段‘验证’的代码
'''执行完装饰器之后，Func1的代码如下:
def Func1(arg):
    print '验证代码'
    print 'func1',arg
'''
result = Func1('text')
print  result