#!/usr/bin/env python
#coding:utf8
'''
Created on 2016-11-5
@Author:Guolikai
'''

def login(username):
    if username == 'glk':
        #print '登陆成功'   #调用函数时，直接打印；
        return '登陆成功'  #调用函数时，需用变量赋值；
    else:
        return '登陆失败'
def message(username):
    print 'Name:%s\nAge:27\nJob:NOC\nsarlary:5000\n' % username
if __name__ == '__main__':
    user = raw_input('请输入用户名：')
    res_msg = login(user)
    if res_msg == '登陆成功':
        message(user)
    else:
        print res_msg

