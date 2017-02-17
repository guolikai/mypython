#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
import load,cpu,memory

def get_load_info():
    return load.monitor()
def get_cpu_status():
    return cpu.monitor()
def get_memory_info():
    return memory.monitor()