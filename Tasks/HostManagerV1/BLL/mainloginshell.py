#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-1 @Author:Guolikai'''
import sys
import globalsetting
from Model.hostmanager import UserInfo
from passwordinput import PasswordInput
from tryoperation import TryOperation
class LoginShell(object):
    def __init__(self):
        pass
    def Username(self):
        tryoperation = TryOperation()
        return tryoperation.TryOperationInput('\033[35;1m请输入您的用户名:\033[0m')
    def Password(self):
        pwd = PasswordInput()
        return pwd.PasswordInputMain()
    def UserCheck(self,username,password):
        userinfo = UserInfo()
        match_result = len(userinfo.SelectMatchDict(username,password))
        if match_result ==0:
            return 'User Match Failed'
        else:
            return 'User Match Success'
    def UserExit(self,username):
        self.sys.exit('\033[33;5m您已退出主机管理系统！\033[0m')

    def LoginShellMain(self,user,passwd):
        result =  self.UserCheck(user,passwd)
        if result=='User Match Success':
            print '\033[32;5m###    欢迎使用HostManager系统   ###\033[0m'
        else:
            print '用户名或密码错误，请重新登录！'

if __name__ == '__main__':
    loginshell = LoginShell()
    user = loginshell.Username()
    passwd = loginshell.Password()
    loginshell.LoginShellMain(user,passwd)

