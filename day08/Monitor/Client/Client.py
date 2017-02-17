#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import threading,pickle,time
from RedisHelper import RedisHelper
from plugins import PluginApi


host_ip = '172.16.1.100'
class MonitorClient(object):
    def __init__(self,server,port):
        self.server = server
        self.port = port
        self.configs = {}
        self.redis = RedisHelper()

    def GetConfigs(self):
        config = self.redis.Get('HostConfig::%s' %  host_ip)
        if config:
            self.configs =  pickle.loads(config)
            return True
    def Handle(self):
        if self.GetConfigs():
            print '---Going to monitor services---',self.configs
            while True:
                for service_name,val in self.configs['services'].items():
                    interval,plugin_name,lask_check = val
                    if time.time() - lask_check >= interval:
                    #Need to kick off the next run
                        t =threading.Thread(target=self.Task,args=[service_name,plugin_name])
                        t.start()
                        self.configs['services'][service_name][2] = time.time()
                    else:
                        next_run_time = interval - (time.time()-lask_check)
                        print '\033[32,5m%s\033[0m will be in next \033[32,5m%s\033[0m seconds' % (service_name,next_run_time)
                time.sleep(1)
        else:
            print '---Could not find any configrations for this host---'
    def format_msg(self,key,value):
        #pickle序列化
        msg = {key,value}
        return  pickle.dumps(msg)
    def Task(self,service_name,plugin_name):
        print '------Going into run Service:',service_name,plugin_name
        func = getattr(PluginApi,plugin_name)
        result = func()
        msg = self.format_msg('report_service_data',
                              {'ip':host_ip,
                               'service_name':service_name,
                               'data':result,
                               })
        self.redis.Public(msg)
    def Run(self):
        self.Handle()

if __name__ == '__main__':
    cli = MonitorClient('yourmonitorserverip','port')
    cli.Run()