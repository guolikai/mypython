#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-10-27 @Author:Guolikai'''
import getpass
pwd = getpass.getpass('password: ')
print pwd

'''
import msvcrt, sys
def pwd_input():
  chars = []
  while True:
    newChar = msvcrt.getch()
    if newChar in '\r\n':
    # 如果是换行，则输入结束
      print ''
      break
    elif newChar == '\b':
    # 如果是退格，则删除末尾一位
      if chars:
        del chars[-1]
        sys.stdout.write('\b')
        # 删除一个星号，但是不知道为什么不能执行...
    else:
      chars.append(newChar)
      sys.stdout.write('*')
      # 显示为星号
  print ''.join(chars)
pwd = pwd_input()
print pwd'''
