#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
import socket,sys,os,time
ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(ip_port)
def Sendfile(obj,file_size,file_name):
    f = file(file_name, 'rb')
    send_size = 0
    Flag = True
    while Flag:
        if send_size + 1024 > file_size:
            data = f.read(file_size - send_size)
            Flag = False
        else:
            data = f.read(1024)
            send_size += 1024
        obj.send(data)
        return 'Upload Done'
    f.close()

while True:
    input = raw_input('path:[put|/etc/passwd]')
    if len(input) == 0:
        continue
    cmd, path = input.split('|')
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    sk.send(cmd + "|" + file_name + '|' + str(file_size))
    print 'Going to send...'
    time.sleep(0.1)
    if Sendfile(sk,file_size,path) == 'Upload Done':
        print 'Upload Done'
	print sk.recv(1024)
sk.close()
