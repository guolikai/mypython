M#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
conn_dict = dict(host='127.0.0.1', user='root', passwd='123456', db='mysql', port=3306)

def ProcessFee(money):
    percentage = "%5"
    return money * float(percentage.replace("%", "")) / 1000

raw = int(input('Please input a number:'))
print type(raw)
print raw
print ProcessFee(9880)
print raw-ProcessFee(9880)