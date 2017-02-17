#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-5
@Author:Guolikai'''
import random

def number6():
    code = []
    for i in range(6):
        if i == random.randint(1,5):
            code.append(str(random.randint(1,9)))
        else:
            temp = random.randint(65,90)
            code.append(chr(temp))
    return ''.join(code)
if __name__ == '__main__':
    print number6()
