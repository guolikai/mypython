#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import socket
def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 ok\r\n")
    client.send("Content-Type:text/html\r\n\r\n")
    client.send("<a href='www.baidu.com'> Hello,Serven </a>")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8080))
    sock.listen(5)
    while True:
        connection,address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()