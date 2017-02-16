#!/usr/bin/python
#coding:utf8
import re
File = raw_input("请输入要查找的文件：")
Word = raw_input("请输入要查找文件内的单词：")
count = 0
Find = file(File,'r')
for s in Find.readlines():
    li = re.findall(Word,s)
#    count = 0 
    if len(li) > 0:
        count = count+len(li)
print '你要查找文件的单词总数是:'
print count
Find.close()

