#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
import SocketServer,os
def recv_all(obj,file_size,file_name):
    recv_size = 0
    f = file(file_name, 'wb')
    Flag = True
    while Flag:    ## 未上传完毕
        if int(file_size) > recv_size:
            # 最多接收1024，可能接收的小于1024
            data = obj.recv(1024)
            recv_size += len(data)
        # 上传完毕，则退出循环
        else:
            recv_size = 0
            Flag = False
            continue
        f.write(data)  # 写入文件
	print 'Recv successed.'
        return  'Done'
    f.close()

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = '/tmp'
        conn = self.request
        print 'Got a new connection from',self.client_address
	while True:
            pre_data = conn.recv(1024)   # 获取请求方法、文件名、文件大小
            cmd,file_name,file_size = pre_data.split('|')
            file_dir = os.path.join(base_path, file_name)  # 上传文件路径拼接
            if cmd=='put':
                write_to_file = recv_all(self.request,int(file_size),file_dir)
                if write_to_file == 'Done':
                    conn.send('Client Upload Success!\n')
	conn.close()
if __name__ == '__main__':
    instance = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    instance.serve_forever()
