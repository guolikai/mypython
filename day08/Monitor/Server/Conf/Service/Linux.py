#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
#监控项
import sys
sys.path.append('/root/python/day08/Monitor/conf/Service')
import Generic
from data_process import avg,hit,last
class CPU(Generic.BaseService):
    def __init__(self):
        super(CPU,self).__init__()
        self.name = 'linux_cpu'
        self.interval = 30
        self.last_time = 0
        self.plugin_name = 'get_cpu_status'
        self.triggers = {
            'idle':{'func':avg,
                    'minutes':15,
                    'operator':'lt',
                    'warning':20,
                    'critical':15,
                    'data_type':'percentage'
                    },
            'iowait': {'func': hit,
                     'minutes': 10,
                     'operator':'gt',
                     'threshold':3,
                     'warning':50,
                     'critical': 80,
                     'data_type': 'int'
                      }
            }
class Memory(Generic.BaseService):
    def __init__(self):
        super(Memory, self).__init__()
        self.name = 'linux_memory'
        self.interval = 30
        self.last_time = 0
        self.plugin_name = 'get_memory_info'
        self.triggers = {
            'usage': {'func': avg,
                       'minutes': 15,
                       'operator': 'gt',
                       'warning': 80,
                       'critical':90,
                       'data_type':'percentage'
                       }
            }

if __name__ == '__main__':
    c = CPU()
    print c.name,c.interval,c.plugin_name