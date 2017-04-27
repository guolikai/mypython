#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
import globalsetting
from hostmanager import HostGroups,HostUserPasswd
from tryoperation import TryOperation
from remotecommand import RemoteCommand
from demoipconnect import DemoIpConnect

import sys
import time
import paramiko
class UserOPS(object):
    def __init__(self):
        pass
    def UserOperation(self):
        print '\033[32;5m###    欢迎使用HostManager系统   ###\033[0m'
        message = ['输入ID直接登录','显示您有权限的主机','显示您有权限的主机组','显示组下的主机','批量执行命令','批量上传文件','批量下载文件','退出']
        for item in enumerate(message,1):
            print item[0],item[1]
        tryoperation = TryOperation()
        while True:
            your_choice = tryoperation.TryOperationInt('您接下来的操作[1-8]:')
            if your_choice  in range(9):
                return message[your_choice-1]
            else:
                print '\033[32;5m输入的数字超过范围，请在[1-8]选择\033[0m'
                continue
    def InputIp(self):
        ip = raw_input('输入Ip地址登录:')
        return ip
    def CheckIp(self,username,ip):
        hostgroups = HostGroups()
        match_result = len(hostgroups.SelectCheckIp(username,ip))
        if match_result == 0:
            if len(hostgroups.SelectIps(ip)) == 0:
                print '主机[%s],不存在' % ip
            else:
                print '主机[%s],您的权限不够' % ip
        else:
            return 'CheckIp Success'

    def GetAuthHost(self,username):
        #显示您有权限的主机
        hostgroups = HostGroups()
        data = hostgroups.SelectUsernameIps(username)
        for i in range(len(data)):
            print data[i]['ip']

    def GetAuthHostgroup(self, username):
        #显示您有权限的主机组
        hostgroups = HostGroups()
        data = hostgroups.SelectHostgroup(username)
        for i in range(len(data)):
            print data[i]['hostgroup']

    def GetHostgroupIP(self,username):
        #显示组下的主机
        tryoperation = TryOperation()
        group = tryoperation.TryOperationInput('输入查询的主机组:')
        hostgroups = HostGroups()
        data = hostgroups.SelectHostgroupIp(username,group)
        #print data
        if len(data)==0:
            if len(hostgroups.SelectHostgroup(group)) == 0:
                print '主机组[%s],不存在' % group
            else:
                print '主机组[%s],您的权限不够' % group
        else:
            for i in range(len(data)):
                print data[i]['ip']

    def UserOpsMain(self,username):
        while True:
            result = self.UserOperation()
            if result == '输入ID直接登录':
                DemoIpConnect(username)
            elif result == '显示您有权限的主机':
                self.GetAuthHost(username)
            elif result == '显示您有权限的主机组':
                self.GetAuthHostgroup(username)
            elif result == '显示组下的主机':
                self.GetHostgroupIP(username)
            elif result == '批量执行命令':
                remotecommand = RemoteCommand()
                remotecommand.RemoteCommandMain(username)
            elif result == '批量上传文件':
                pass
            elif result == '批量下载文件':
                pass
            else:
                sys.exit('\033[33;5m您已退出主机管理系统！\033[0m')
if __name__ == '__main__':
        username = 'glk'
        userops = UserOPS()
        userops.UserOpsMain(username)
