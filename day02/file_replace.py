#!/usr/bin/env python
#_*_ coding:utf8  _*_
import sys,os
if len(sys.argv) <= 4:
    print 'Usage:./file_replace.py old_text new_text file_name'
old_text,new_text= sys.argv[1],sys.argv[2]
file_name = sys.argv[3]

f = file(file_name,'rb')
new_file = file('.%s.bak' % file_name,'wb')   #打开新文件
for line in f.xreadlines():                   #循环旧文件并替换   
   # print line.replace(old_text,new_text)
    new_file.write(line.replace(old_text,new_text))
f.close()
new_file.close()

if '--bak' in sys.argv:
    os.rename(file_name,'%s.bak' % file_name)
    os.rename('.%s.bak' % file_name , file_name)
else:
    os.rename('.%s.bak' % file_name , file_name)
