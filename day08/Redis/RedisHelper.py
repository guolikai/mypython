#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-12-10 @Author:Guolikai'''
#http://blog.csdn.net/javastart/article/details/40425951
import  redis
class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')
        self.chan_sub='FM87.7'
        self.chan_pub='FM100.0'
    def Get(self,key):
        return self.__conn.get(key)
    def Set(self,key,value):
        self.__conn.set(key,value)
    def Public(self,msg):
        self.__conn.publish(self,chan_pub,msg)
        return True
    def Subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
if __name__ == '__main__':
    t = RedisHelper()
    t.Public('test')