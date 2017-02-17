#!/usr/bin/env python
#_*_ coding:utf8  _*_
nameInfo = {
'name':'glk',
'age':27,
'Job':'IT',
'address':'BeiJing'
}

for i in nameInfo:
    print i     #默认只打印key

for i in nameInfo:
    print i,nameInfo[i]     #打印key,volues，效率高

for k,v in nameInfo.items():
    print  k,v			#打印key,volues,效率低
