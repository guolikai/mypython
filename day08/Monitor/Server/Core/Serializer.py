#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import globel_setting
from Conf import Hosts
import pickle,time
from RedisHelper import RedisHelper
def host_config_serializer(host_ip):
    applied_services = []
    configs = {
        'services':{},
        #'reflush_configs_interval':
    }
    for group in Hosts.monitored_groups:
        if host_ip in group.hosts:
            applied_services.extend(group.services)
    applied_services = set(applied_services)   #列表去重
    for service in applied_services:
        service = service()
        configs['services'][service.name]=[service.interval,service.plugin_name,0]
    return configs

def all_flush_configs_into_redis():
    applied_hosts = []
    redis = RedisHelper()
    for group in Hosts.monitored_groups:
        applied_hosts.extend(group.hosts)
    applied_hosts = set(applied_hosts)  # 列表去重
    for host_ip in applied_hosts:
        host_config = host_config_serializer(host_ip)
        key = 'HostConfig::%s' %  host_ip
        redis.Set(key,pickle.dumps(host_config))
    return True
def all_host_config():
    configs = {'hosts':{}}
    for group in Hosts.monitored_groups:
        for host_ip in group.hosts:
            #if not configs['hosts'].has_key(host_ip)
            configs['hosts'][host_ip] = {}
    return configs

def report_service_data(server_instance,msg):
    host_ip = msg['ip']
    service_ststus_data = msg['data']
    service_name = msg['service_name']
    server_instance.hosts['host'][host_ip][service_name] = {'data':service_ststus_data,'time_stamp':time.time()}
    key = 'StatusData::%s' % host_ip
    server_instance.redis.set(key,pickle.dumps(server_instance.hosts['host'][host_ip][service_name]))

if __name__ == '__main__':
    #print host_config_serializer('172.16.1.110')
    all_flush_configs_into_redis()


