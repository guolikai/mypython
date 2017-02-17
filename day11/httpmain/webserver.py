#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import socket
#应用程序
'''WSGI（Web Server Gateway Interface）是一种规范，
它定义了使用python编写的web app与web server之间接口格式，实现web app与web server间的解耦。
python标准库提供的独立WSGI服务器称为wsgiref。'''
def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello, Seven")

#服务程序
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()