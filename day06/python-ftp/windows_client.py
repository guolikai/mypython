#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-26 @Author:Guolikai'''
import socket,sys,os,time
ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(ip_port)
container = {'key': '', 'data': ''}
while True:
    input = raw_input('path:')
    cmd, path = input.split('|')
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    sk.send(cmd + "|" + file_name + '|' + str(file_size))
    time.sleep(0.1)
    send_size = 0
    f = file(path, 'rb')
    Flag = True
    while Flag:
        if send_size + 1024 > file_size:
            data = f.read(file_size - send_size)
            Flag = False
        else:
            data = f.read(1024)
            send_size += 1024
        sk.send(data)
    f.close()
sk.close()