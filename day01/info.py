#!/usr/bin/env python
#_*_ coding:utf8 _*_
name = raw_input('Please input your Name:')
age = input('Age:')     #input()表示原生输入：输入数字就是数字，字符是字符，变量会调用定义的变量;
job = raw_input('Job:')
salary = raw_input('Salary:')
if age > 40:
  msg = 'Your age is too old.'
elif age > 30:
  msg = 'Your age is young,you have a few years to xx up.'
else:
  msg = 'You are still quite young,go hook up some girls.' 

print '''
Private Information Of %s:
	Name: %s
	Age:  %s
	Job:  %s
     Salary:  %s
----------------------------
%s
'''  %  (name,name,age,job,salary,msg)
