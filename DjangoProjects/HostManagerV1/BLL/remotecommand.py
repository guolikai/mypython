#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-5 @Author:Guolikai'''
import globalsetting
from Model.hostmanager import HostGroups,HostUserPasswd

from tryoperation import TryOperation
import paramiko
import sys
import threading

class RemoteCommand(object):
    def BatchExcuComm(self,username):
        message = ['通过IP执行', '通过Group执行', '通过Network执行']
        for item in enumerate(message, 1):
            print item[0], item[1]
        tryoperation = TryOperation()
        while True:
            your_choice = tryoperation.TryOperationInt('您接下来的操作[1-3]:')
            if your_choice in range(4):
                return message[your_choice - 1]
            else:
                print '\033[32;5m输入的数字超过范围，请在[1-8]选择\033[0m'
                continue
    def RemoteIpComm(slef,host,user,pwd,comm):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host,username=user, password=pwd)
        except Exception,e:
            print '%s: Connection Refused' % host
        else:
            stdin, stdout, stderr = ssh.exec_command(comm)
            out = stdout.read()
            err = stderr.read()
            if out:
                print "%s: %s" % (host, out),
            if err:
                print "%s: %s" % (host, err),
        ssh.close()
    def RemoteNetworkCommMain(self,username):
            if len(sys.argv) != 5:
                print "Usage: %s ip_network user password 'comm'" % sys.argv[0]
                sys.exit(1)
            user = sys.argv[2]
            password = sys.argv[3]
            comm = sys.argv[4]
            ips = ["%s.%s" % (sys.argv[1], i) for i in range(1, 255)]
            remotecomm = RemoteCommand()
            for ip in ips:
                t = threading.Thread(target=self.RemoteIpComm, args=(ip, user, password, comm))
                t.start()
    def CheckIp(self,username,ip,):
        hostgroups = HostGroups()
        match_result = len(hostgroups.SelectCheckIp(username,ip))
        if match_result == 0:
            if len(hostgroups.SelectIpExist(ip)) == 0:
                # sys.exit('主机[%s],不存在' % ip)
                print '主机[%s],不存在' % ip
            else:
                print '主机[%s],您的权限不够' % ip
        else:
            return ip
    def IpList(self,username):
        tryoperation = TryOperation()
        ip_list = []
        while True:
            ipaddr = tryoperation.TryOperationInput('输入要批量操作的IP:')
            ips = ipaddr.strip(" ").split()
            for i in range(len(ips)):
                host = ips[i]
                ip = self.CheckIp(username,host)
                ip_list.append(ip)
            if tryoperation.TryOperationChoice('是否继续输入Ip') == 'n':
                return ip_list
            else:
                continue

    def Command(self):
        tryoperation = TryOperation()
        comm = tryoperation.TryOperationInput('输入要批量执行的命令:')
        return comm
    def RemoteIpCommMain(self,username):
        user = 'root'
        comm = self.Command()
        hostuserpasswd = HostUserPasswd()
        ip_list =  self.IpList(username)
        for i in range(len(ip_list):
            ip = ip_list[i]
            pwd = hostuserpasswd.SelectPassword(ip,user)
            t = threading.Thread(target=self.RemoteIpComm,args=(ip,user,pwd,comm))
            t.start()

    def GroupList(self,username):
        ip_list = []
        tryoperation = TryOperation()
        hostgroups = HostGroups()
        while True:
            hostgroups = tryoperation.TryOperationInput('输入查询的主机组:')
            hostgroup = hostgroups.strip(" ").split()
            for i in range(len(hostgroup)):
                host = hostgroup[i]
                data = hostgroups.SelectHostgroupIp(username, group)
                if len(data) == 0:
                    if len(hostgroups.SelectHostgroup(group)) == 0:
                        print '主机组[%s],不存在' % group
                    else:
                        print '主机组[%s],您的权限不够' % group
                else:
                    for i in range(len(data)):
                        ip = data[i]['ip']
                        ip_list.append(ip)
            if tryoperation.TryOperationChoice('是否继续输入Ip') == 'n':
                return ip_list
            else:
                continue
    def RemoteGroupCommMain(self,username):
        user = 'root'
        comm = self.Command()
        hostuserpasswd = HostUserPasswd()
        ip_list = self.GroupList(username)
        for i in range(len(ip_list):
            ip = ip_list[i]
            pwd = hostuserpasswd.SelectPassword(ip, user)
            t = threading.Thread(target=self.RemoteIpComm, args=(ip, user, pwd, comm))
            t.start()
    def RemoteCommandMain(self,username):
        while True:
            result = self.BatchExcuComm(username)
            if result == '通过IP执行':
                self.RemoteIpCommMain(username)
            elif result == '通过Group执行':
                self.RemoteGroupCommMain(username)
            else:
                self.RemoteNetworkCommMain(username)





