#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-8
@Author:Guolikai'''

#输入格式： XXX/XXX    account/login
'''
data = raw_input('请输入地址：')
array = data.split('/')
from backend import account
if data == 'account/login':
    account.login()
else:
    account.logout()
'''
#用反射关系来调用；
'''
data = raw_input('请输入地址：')
array = data.split('/')
userput = __import__('backend.'+array[0])
module = getattr(userput,array[0])
func = getattr(module,array[1])
func()'''

#异常处理
try:
    data = raw_input('请输入地址：')
    array = data.split('/')
    userput = __import__('backend.'+array[0])
    module = getattr(userput,array[0])
    func = getattr(module,array[1])
    func()
except ImportError,e:
    print 1,e
    print '跳转到自定义的404'
except AttributeError,e:
    print 2,e
    print '跳转到自定义的404'
except Exception,e:
    print 3, e
    print '跳转到自定义的404'
else:
    print '没有出错！'
finally:
    print '无论异常与否，都执行！'