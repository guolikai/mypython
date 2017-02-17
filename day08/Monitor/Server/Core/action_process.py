#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import pickle
import Serializer
def action_process(server_instance,msg):
    msg = pickle.loads(msg[2])
    print msg
    func_name = msg.keys()[0]
    func = getattr(Serializer,func_name)
    func(server_instance,msg[func_name])
