#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-1 @Author:Guolikai'''
import sys
import globalsetting
from Utility.sqlhelper import MysqlHelper
'''Userinfo堡垒机用户登录表结构：user_id,username,password,remarks'''
class UserInfo(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def SelectMatchDict(self,username,password):
        sql = 'select username,password from hostmanager.userinfo where username=%s and password=%s'
        params = (username,password)
        return self.__helper.SelectDict(sql,params)
    def InsertUserinfo(self,username,password):
        sql = 'insert into hostmanager.userinfo (username,password) values(%s,%s)'
        params = (username,password)
        return self.__helper.Insert(sql,params)
    def DeleteUserinfoUsername(self,username,password):
        sql = 'delete hostmanager.userinfo where username=%s and password=%s'
        params = (username,password)
        return self.__helper.Delete(sql,params)
    def UpdateUserinfoUsername(self,username,password,new_username):
        sql = 'update  hostmanager.userinfo set username=%s where username=%s and password=%s'
        params = (new_username,password,username)
        return self.__helper.Update(sql,params)
    def UpdateUserinfoPassword(self,username,password,new_password):
        sql = 'update  hostmanager.userinfo set password=%s  where username=%s and password=%s'
        params = (new_password,username,password,)
        return self.__helper.Update(sql,params)

'''HostGroups服务器主机组表结构:id,ip,hostname,port,hostgroup,username,remarks'''
class HostGroups(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def SelectUsernameIps(self, username):
        sql = 'select distinct ip from hostmanager.hostgroups where username=%s'
        params = (username)
        return self.__helper.SelectDict(sql, params)
    def SelectIpExist(self,ip):
        sql = 'select distinct ip from hostmanager.hostgroups where ip=%s'
        params = (ip)
        return self.__helper.SelectDict(sql, params)
    def SelectCheckIp(self, username,ip):
        sql = 'select username,ip from hostmanager.hostgroups where username=%s and ip=%s'
        params = (username,ip)
        return self.__helper.SelectDict(sql, params)

    def SelectHostgroups(self,hostgroup):
        sql = 'select  distinct hostgroup from hostmanager.hostgroups where hostgroup=%s'
        params = (hostgroup)
        return self.__helper.SelectDict(sql, params)

    def SelectHostgroup(self, username):
        sql = 'select  distinct hostgroup from hostmanager.hostgroups where username=%s'
        params = (username)
        return self.__helper.SelectDict(sql, params)
    def SelectCheckHostgroup(self, username,hostgroup):
        sql = 'select username,hostgroup from hostmanager.hostgroups where username=%s and hostgroup=%s'
        params = (username,hostgroup)
        return self.__helper.SelectDict(sql, params)
    def SelectHostgroupIp(self,username,hostgroup):
        sql = 'select ip from hostmanager.hostgroups where username=%s and hostgroup=%s'
        params = (username,hostgroup)
        return self.__helper.SelectDict(sql, params)

'''HostUserPassword服务器用户密码表结构:id,ip,username,password，remarks'''
#HostUserPassword用于远程连接主机时，验证登录用的；
class HostUserPasswd(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def SelectHostUsernamePassword(self,ip):
        sql = 'select username,password from hostmanager.hostuserpassword  where ip=%s'
        params = (ip)
        return self.__helper.SelectDict(sql, params)
    def SelectIdUsername(self,ip):
        sql = 'select id,username from hostmanager.hostuserpassword  where ip=%s'
        params = (ip)
        return self.__helper.SelectDict(sql, params)
    def SelectUsernamePassword(self, ip,id):
        sql = 'select username,password from hostmanager.hostuserpassword  where ip=%s and id=%s'
        params = (ip,id)
        return self.__helper.SelectDict(sql, params)
    def SelectPassword(self, ip,username):
        sql = 'select password from hostmanager.hostuserpassword  where ip=%s and username=%s'
        params = (ip,username)
        return self.__helper.SelectDict(sql, params)
'''UserLogs用户日志审计记录:id,user,time,username,ip,cmd,remarks'''
#UserLogs用户远程连接主机时，操作记录；
class UserLogs(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def SelectUser(self,user):
        sql = 'select user,time,username,ip,cmd from hostmanager.userlogs  where user=%s'
        params = (user)
        return self.__helper.SelectDict(sql,params)
    def SelectUserIp(self,user,ip):
        sql = 'select user,time,username,ip,cmd from hostmanager.userlogs  where user=%s and ip=%s'
        params = (user,ip)
        return self.__helper.SelectDict(sql,params)
    def InsertInto(self,user,time,username,ip,cmd):
        sql = 'insert into hostmanager.userlogs(user,time,username,ip,cmd) values(%s,%s,%s,%s,%s)'
        params = (user,time,username,ip,cmd)
        return self.__helper.Insert(sql,params)
'''
if __name__ == '__main__':
    hostgroups = HostGroups()
    username = 'glk'
    ip = '172.16.1.101'
    print  hostgroups.SelectCheckIp(username,ip)
    #print  hostgroups.SelectIp(username)
    hostuserpassword = HostUserPasswd()
    ip = '172.16.1.101'
    print  hostuserpassword.SelectHostUsernamePassword(ip)
    '''
