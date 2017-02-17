#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
class TryOperation(object):
    def __init__(self):
        pass
    def TryOperationInput(self,operation):
        while True:
            try:
                your_choice = raw_input('%s' % operation )
            except KeyboardInterrupt, e:
                print "您本次操作取消" 
                continue
            except Exception,e:
                print "您的输入有误，请重新输入"
            else:
                return your_choice
    def TryOperationChoice(self,operation):
        while True:
            try:
                your_choice = raw_input('%s' % operation )
                if your_choice=='y' or your_choice=='n':
                    return your_choice
            except KeyboardInterrupt, e:
                print "您本次操作取消" 
                continue
            except Exception,e:
                print "您的输入有误，请重新输入"
            else:
                print "您的输入有误，请重新输入"
    def TryOperationInt(self,operation):
        while True:
            try:
                your_choice = int(raw_input('%s' % operation ))
            except KeyboardInterrupt, e:
                print "您本次操作取消" 
                continue
            except Exception,e:
                print "您的输入有误，请重新输入"
            else:
                return your_choice

    def TryOperationFloat(self, operation):
        while True:
            try:
                your_choice = float(raw_input('%s' % operation))
            except KeyboardInterrupt, e:
                print "您本次操作取消"
                continue
            except Exception, e:
                print "您的输入有误，请重新输入"
            else:
                return your_choice