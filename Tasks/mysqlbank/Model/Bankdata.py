#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
import sys
sys.path.append('/root/python/mysqlbank')
from Utility.SqlHelper import MysqlHelper
class UserInfo(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def SelectUsername(self,username):
        sql = 'select * from bankdata.userinfo where username=%s'
        params = (username,)
        return self.__helper.SelectDict(sql,params)

    def SelectPassword(self,username):
        sql = 'select password from bankdata.userinfo where username=%s'
        params = (username,)
        data = self.__helper.SelectDict(sql,params)
        return data[0]['password']

    def SelectCurrentMoney(self,username):
        sql = 'select current_money from bankdata.userinfo where username=%s'
        params = (username,)
        data = self.__helper.SelectDict(sql,params)
        return data[0]['current_money']

    def SelectCreditMoney(self,username):
        sql = 'select credit_money from bankdata.userinfo where username=%s'
        params = (username,)
        data = self.__helper.SelectDict(sql,params)
        return data[0]['credit_money']

    def SelectMatchDict(self,username,password):
        sql = 'select username,password from bankdata.userinfo where username=%s and password=%s'
        params = (username,password)
        return self.__helper.SelectDict(sql,params)

    def InsertUserinfo(self,username,password,current_money,credit_money):
        sql = 'insert into bankdata.userinfo (username,password,current_money,credit_money) values(%s,%s,%s,%s)'
        params = (username,password,current_money,credit_money)
        return self.__helper.Insert(sql,params)
    def DeleteUserinfoUsername(self,username):
        sql = 'delete bankdata.userinfo where username=%s'
        params = (username)
        return self.__helper.Delete(sql,params)
    def UpdateUserinfoUsername(self,username,new_username):
        sql = 'update  bankdata.userinfo set username=%s where username=%s'
        params = (new_username,username)
        return self.__helper.Update(sql,params)
    def UpdateUserinfoPassword(self,username,new_password):
        sql = 'update  bankdata.userinfo set password=%s  where username=%s'
        params = (new_password,username)
        return self.__helper.Update(sql,params)
    def UpdateUserinfoCurrentMoney(self,username,current_money):
        sql = 'update  bankdata.userinfo set current_money=%s where username=%s'
        params = (current_money,username)
        return self.__helper.Update(sql,params)
    def UpdateUserinfoCreditMoney(self,username,credit_money):
        sql = 'update  bankdata.userinfo set credit_money=%s where username=%s'
        params = (credit_money,username)
        return self.__helper.Update(sql,params)

class UserLocked(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def SelectUsernameOne(self,username):
        sql = 'select * from bankdata.userlocked where username=%s'
        params = (username)
        return self.__helper.SelectOne(sql,params)
    def SelectUsernameDict(self,username):
        sql = 'select * from bankdata.userlocked where username=%s'
        params = (username)
        return self.__helper.SelectDict(sql,params)
    def InsertUsername(self,username):
        sql = 'insert into  bankdata.userlocked(username) values(%s)'
        params = (username)
        return self.__helper.Insert(sql,params)
    def DeleteUsername(self,username):
        sql = 'delete  bankdata.userlocked where username=%s'
        params = (username)
        return self.__helper.Delete(sql,params)
    def UpdateUsername(self,old,new):
        sql = 'update  bankdata.userlocked set username=%s where username=%s'
        params = (new,old)
        return self.__helper.Update(sql,params)



class AccountDetails(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def SelectAccountDetails(self,username):
        sql = 'select * from bankdata.accountdetails where trans_account=%s'
        params = (username)
        return self.__helper.SelectDict(sql, params)
    def InsertAccountDetails(self,trans_date,username,trans_amount,other_account,description):
        sql = 'insert into  bankdata.accountdetails(trans_date,trans_account,trans_amount,other_account,description) values(%s,%s,%s,%s,%s)'
        params = (trans_date,username,trans_amount,other_account,description)
        return self.__helper.Insert(sql, params)
    def DeleteAccountDetails(self, username):
        sql = 'delete bankdata.accountdetails where trans_account=%s'
        params = (username)
        return self.__helper.Delete(sql, params)
    def UpdateAccountDetails(self, trans_amount, username):
        sql = 'update  bankdata.accountdetails set trans_amount=%s where trans_account=%s'
        params = (trans_amount,username)
        return self.__helper.Update(sql, params)
