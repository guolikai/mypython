#!/usr/bin/env python

from random import choice
import string

all_chs = string.letters + string.digits

def gen_pass(num=8):
    pwd = ''

    for i in range(num):
        pwd += choice(all_chs)

    return pwd

if __name__ == '__main__':
    print gen_pass()
    print gen_pass(4)
