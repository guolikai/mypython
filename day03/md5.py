#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-5
@Author:Guolikai'''
import hashlib
hash_md5 = hashlib.md5()
hash_md5.update('admin')
print hash_md5.hexdigest()