#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-8
@Author:Guolikai'''
def filter(before_func,after_func):
    def outer(main_func):    #定义装饰器
        def wrapper(request,kargs):
            before_result = before_func(request,kargs)
            if(before_result !=  None):
                return before_result
            main_result = main_func(request, kargs)
            if (main_result != None):
                return main_result
            after_result = after_func(request, kargs)
            if (after_result != None):
                return after_result
        return  wrapper
    return outer
def Func1(arg1,arg2):
    print 'func1',arg1
    return 'return1'
def Func2(arg1,arg2):
    print 'func2',arg1
    return 'return2'

@filter(Func1,Func2)    #装饰器与函数发生关系
def Func3(arg1,arg2):
    print 'func3',arg1,arg2
    return 'return3'
if __name__ == '__main__':
    print  Func3('text','python')