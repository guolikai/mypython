#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import commands

def monitor(first_invoke=1):
    shell_command = 'sar 1 3 | grep '
    status,result = commands.getstatusoutput(shell_command)
    if status != 0:
        value_dic = {'status':status,'data':result}
    else:
        value_dic = {}
        user,nice,system,iowait,steal,idle,status = result[:]
        value_dic = {
            'user':user,
            'nice',nice,
            'system',system,
            'iowait',iowait,
            'steal',steal,
            'idle',idle,
            'status',status
        }
    return  value_dic