#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-1 @Author:Guolikai'''
import os,sys
import globalsetting
from Model.hostmanager import UserLogs,HostUserPasswd,HostGroups
from tryoperation import  TryOperation
import base64
from binascii import hexlify
import getpass
import select
import socket
import time
import traceback
import paramiko

import termios
import tty
def posix_shell(chan,user,username,ip):
    import select
    oldtty = termios.tcgetattr(sys.stdin)
    userlogs = UserLogs()
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        records = []
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = chan.recv(1024)
                    if len(x) == 0:
                        print '\r\n*** EOF\r\n',
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                records.append(x)
                if x == '\r':
                    c_time = time.strftime('%Y-%m-%d %H:%M:%S')
                    cmd = ''.join(records).replace('\r','')
                    userlogs.InsertInto(user,c_time,username,ip,cmd)
                    records = []
                if len(x) == 0:
                    break
                chan.send(x)
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

def agent_auth(transport, username):
    """Attempt to authenticate to the given transport using any of the private
keys available from an SSH agent."""
    agent = paramiko.Agent()
    agent_keys = agent.get_keys()
    if len(agent_keys) == 0:
        return
    for key in agent_keys:
        print 'Trying ssh-agent key %s' % hexlify(key.get_fingerprint()),
        try:
            transport.auth_publickey(username, key)
            print '... success!'
            return
        except paramiko.SSHException:
            print '... nope.'
def autoconnect(t,username, hostname,passwd):
    t.auth_password(username, passwd)

def CheckIp(username):
    while True:
        tryoperation = TryOperation()
        ip  = tryoperation.TryOperationInput('输入Ip地址登录:')
        hostgroups = HostGroups()
        match_result = len(hostgroups.SelectCheckIp(username,ip))
        if match_result == 0:
            if len(hostgroups.SelectIpExist(ip)) == 0:
                print '主机[%s],不存在' % ip
            else:
                print '主机[%s],您的权限不够' % ip
            continue
        else:
            #return 'CheckIp Success'
	        return ip

def DemoIpConnect(user):
    hostname  =  CheckIp(user)
    port = 22
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((hostname, port))
    except Exception, e:
        print '*** Connect failed: ' + str(e)
        traceback.print_exc()
        sys.exit(1)
    try:
        t = paramiko.Transport(sock)
        try:
            t.start_client()
        except paramiko.SSHException:
            print '*** SSH negotiation failed.'
            sys.exit(1)

        try:
            keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        except IOError:
            try:
                keys = paramiko.util.load_host_keys(os.path.expanduser('~/ssh/known_hosts'))
            except IOError:
                print '*** Unable to open host keys file'
                keys = {}

        # check server's host key -- this is important.
        key = t.get_remote_server_key()
        if not keys.has_key(hostname):
            print '*** WARNING: Unknown host key!'
        elif not keys[hostname].has_key(key.get_name()):
            print '*** WARNING: Unknown host key!'
        elif keys[hostname][key.get_name()] != key:
            print '*** WARNING: Host key has changed!!!'
            sys.exit(1)
        else:
            print '*** Host key OK.'
            
        default_username = getpass.getuser()
        userops =  HostUserPasswd()
        result = userops.SelectIdUsername(hostname)
        user_list = []
        for i in range(len(result)):
            dict = result[i]
            print i, dict['username']
            user_list.append(dict['username'])
        print '授权系统用户超过1个，请输入ID, q退出'
        your_choice = raw_input('ID>:')
        #print user_list[int(your_choice)]
        if your_choice == 'q':
            sys.exit('\033[33;5m您已退出主机管理系统！\033[0m')
        elif int(your_choice) in range(len(result)):
            ID = result[int(your_choice)]['id']
            hostuserpasswd = HostUserPasswd()
            data = hostuserpasswd.SelectUsernamePassword(hostname,ID)
            for i in range(len(data)):
                dict = data[i]
                username = dict['username']
                password = dict['password']
                agent_auth(t, username)
                if not t.is_authenticated():
                   # manual_auth(t,username, hostname,password)
		            autoconnect(t,username, hostname,password)
                if not t.is_authenticated():
                    print '*** Authentication failed. :('
                    t.close()
                    sys.exit(1)
        
        chan = t.open_session()
        chan.get_pty()
        chan.invoke_shell()
        print '*** Here we go!'
        posix_shell(chan,user,username,hostname)
        chan.close()
        t.close()

    except Exception, e:
        print '*** Caught exception: ' + str(e.__class__) + ': ' + str(e)
        traceback.print_exc()
        try:
            t.close()
        except:
            pass
        sys.exit(1)
if __name__ == '__main__':
    user = 'root'
    DemoIpConnect(user)
