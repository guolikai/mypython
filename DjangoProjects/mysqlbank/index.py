#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
import sys
sys.path.append('/root/python/mysqlbank')
from BLL.AccountLogin import AccountLoginMain
from BLL.AccountSavings import AccountSavingsMain

if __name__ == '__main__':
    while True:
		try:
			username = raw_input('\033[35;1m请输入用户名:\033[0m')
		except KeyboardInterrupt,e:
			print "您取消本次用户名输入"
			break
		else:
			login_result = AccountLoginMain(username)
			if login_result == 'Login Success':
				AccountSavingsMain(username)
