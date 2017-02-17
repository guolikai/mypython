#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-8
@Author:Guolikai'''

class Person:                       #定义类
    Address = 'On the Globe'       #属于类的属性；静态字段
    def __init__(self,name,sex):    #定义对象，seld相当于类的封装；对象方法
        self.Name = name            #属于对象的属性；动态字段
        self.Sex = sex

if __name__ == '__main__':
    p1 = Person('glk',27)
    print Person.Address    #静态类不能访问动态字段，动态对象可以访问静态字段；建议不用
    print p1.Address,p1.Name,p1.Sex
