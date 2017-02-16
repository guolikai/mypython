#!/usr/bin/env python
# -*- coding: utf8 -*-

import random

all_choice = ['石头', '剪刀', '布']
computer = random.choice(all_choice)
player = raw_input('请出拳(石头/剪刀/布): ')

print "Your choice:", player, "Computer's choice", computer

if computer == '石头':
    if player == '石头':
        print "\033[32;1m平局\033[0m"
    elif player == '剪刀':
        print "\033[31;1mYou LOSE!!!\033[0m"
    else:
        print "\033[31;1mYou WIN!!!\033[0m"
elif computer == '剪刀':
    if player == '石头':
        print "\033[31;1mYou WIN!!!\033[0m"
    elif player == '剪刀':
        print "\033[32;1m平局\033[0m"
    else:
        print "\033[31;1mYou LOSE!!!\033[0m"
else:
    if player == '石头':
        print "\033[31;1mYou LOSE!!!\033[0m"
    elif player == '剪刀':
        print "\033[31;1mYou WIN!!!\033[0m"
    else:
        print "\033[32;1m平局\033[0m"
