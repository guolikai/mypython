#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
import sys
sys.path.append('/root/python/mysqlbank')
from Model.Bankdata import UserLocked,UserInfo
from BLL.PasswordInput import PasswordInput

class AccountLogin(object):
    def __init__(self):
        pass
    def AccountUsername(self):
        return raw_input('\033[35;1m请输入您的账户名:\033[0m')
    def AccountPassword(self):
        pwd = PasswordInput()
        return pwd.PasswordInputMain()
    def AccountNameLock(self):
        userlocked = UserLocked()
        lock_result = len(userlocked.SelectUsernameDict(username))
        if lock_result == 0:
            return 'Account Unlock'
        else:
            sys.exit('\033[31;1m嗨%s,您的账户已被锁定，请联系银行进行解锁!\033[0m' % username)

    def AccountNameExist(self,username):
        userinfo = UserInfo()
        match_result = len(userinfo.SelectUsername(username))
        if match_result == 0:
            print '\033[31;1m嗨%s,您的账户不存在!\033[0m' % username
            return 'Account Unexist'
        else:
            return 'Account Exist'
    def AccountMatch(self,username,password):
        userinfo = UserInfo()
        match_result = len(userinfo.SelectMatchDict(username,password))
        if match_result ==0:
            return 'Account Match Failed'
        else:
            return 'Account Match Success'
    def AccountAddLocked(self,username):
        userlocked = UserLocked()
        lock_result = userlocked.InsertUsername(username)
        if lock_result == 1:
            print  '\033[31;1m嗨%s,您密码输错3次账户被锁，请联系银行进行解锁!\033[0m' % username
    def AccountLogin(self,username):
        retry_limit = 3
        retry_count = 0
        while retry_count < retry_limit:     # 只要重试不超过3次就不断循环
            #password = raw_input('\033[32;1mPassword:\033[0m')
            password = self.AccountPassword()
            match_flag = False  # 默认为False，如果用户match上了，就设置为True
            if self.AccountMatch(username,password)=='Account Match Success':
                match_flag = True  # 相等就把循环外的match_flag变量改为True
                print '\033[32;5m嗨%s,欢迎登陆网上银行!\033[0m' % username
                return 'Login Success'
            else:
                retry_count += 1
                print '账户密码有误，您还有%s机会进行输入！' % (retry_limit-retry_count)
        else:
            AccountAddLocked(username)
    def AccountExit(self,username):
        self.sys.exit('\033[33;5m嗨%s,您已退出网上银行！\033[0m' % username)

    def AccountLoginMain(self,username):
        lock_result = self.AccountNameLock(username)
        if lock_result == 'Account Unlock':
            exist_result = self.AccountNameExist(username)
            if exist_result == 'Account Exist':
                return self.AccountLogin(username)
            else:
                sys.exit()

if __name__ == '__main__':
    Username = AccountLogin()
    username = Username.AccountUsername()
    print username
    #Username.AccountLoginMain(username)
