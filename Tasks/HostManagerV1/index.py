#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-1 @Author:Guolikai'''
import sys
from BLL.tryoperation  import TryOperation
from BLL.mainloginshell import LoginShell
from BLL.mainuserops import UserOPS

def RunMain():
    loginshell = LoginShell()
    user = loginshell.Username()
    passwd = loginshell.Password()
    loginshell.LoginShellMain(user, passwd)
    userops = UserOPS()
    userops.UserOpsMain(user)
if __name__ == '__main__':
    RunMain()
