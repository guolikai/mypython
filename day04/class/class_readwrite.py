#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-8 @Author:Guolikai'''

#调用修改私有字段
class info(object):
    def __init__(self,name,job,sarlary):
        self.name = name
        self.job = job
        self.__sarlary = sarlary                #私有字段
    def __show(self):                           #私有方法
        print 'I am glk'
    @property                                   #只读模式
    def Sarlary(self):
        return self.__sarlary

    @Sarlary.setter                             #读写模式
    def Sarlary(self,value):
        self.__sarlary = value


msg = info('glk','it',30000)
msg._info__show()                         #调用类私有方法

print msg.Sarlary
msg.Sarlary = False
print msg.Sarlary
