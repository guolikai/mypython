#!/usr/bin/env python

from random import choice

all_chs = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
pwd = ''

for i in range(8):
    pwd += choice(all_chs)

print pwd
