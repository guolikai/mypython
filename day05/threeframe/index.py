#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
from model.bankdata import userinfo
def main():
    user = raw_input('Username:')
    pwd = raw_input('Password:')
    userinfo = userinfo()
    result = userinfo.GetDict(user,pwd)
    print result
    if not result:
        print '用户名或密码错误！'
    else:
        print '欢迎登录网上银行系统！'
if __name__ == '__main__':
    main()