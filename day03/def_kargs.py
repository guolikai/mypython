#!/usr/bin/env python
#coding:utf8

def Kargs(**kargs):
    for item in kargs.items():
        print item

if __name__ == '__main__':
    Kargs(name='glk',age=27,job='TI')
