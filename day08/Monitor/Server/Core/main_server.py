#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import globel_setting
from RedisHelper import RedisHelper
import Serializer
import  action_process

class MonitorServer(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.hosts = Serializer.all_host_config()
        self.redis = RedisHelper()
    def handle(self):
        redis_sub = self.redis.Subscribe()
        while True:
            msg = redis_sub.parse_response()
            print 'recv:',msg
            action_process.action_process(self,msg)
            print '---waiting for new msg---'
            #received data
            for host,val in self.hosts['hosts'].items():
                print host,val
    def run(self):
        print '---startting monitor server---'
        self.handle()
    def process(self):
        pass

if __name__ == '__main__':
    s = MonitorServer('redis_ip','8000')
    s.run()