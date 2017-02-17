#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-26 @Author:Guolikai'''
import SocketServer,os
class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = 'E:/'
        conn = self.request
        print 'connected...'
        while True:
            pre_data = conn.recv(1024)
            # 获取请求方法、文件名、文件大小
            cmd, file_name, file_size = pre_data.split('|')
            # 已经接收文件的大小
            recv_size = 0
            # 上传文件路径拼接
            file_dir = os.path.join(base_path, file_name)
            f = file(file_dir, 'wb')
            Flag = True
            while Flag:
                # 未上传完毕，
                if int(file_size) > recv_size:
                    # 最多接收1024，可能接收的小于1024
                    data = conn.recv(1024)
                    recv_size += len(data)
                # 上传完毕，则退出循环
                else:
                    recv_size = 0
                    Flag = False
                    continue
                # 写入文件
                f.write(data)
            print 'upload successed.'
            f.close()
if __name__ == '__main__':
    instance = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    instance.serve_forever()