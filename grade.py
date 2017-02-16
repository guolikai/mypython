#!/usr/bin/env python
# -*- coding: utf8 -*-
'''score = int(raw_input("score: "))
if score >= 90:
    print "优秀"
elif score >= 80:
    print "好"
elif score >= 70:
    print "良"
elif score >= 60:
    print "及格"
else:
    print "你要努力了！"
'''
score = int(raw_input("score: "))
if score >= 60 and score < 70:
    print "及格"
elif 70 <= score < 80:
    print "良"
elif 80 <= score < 90:
    print "好"
elif score >= 90:
    print "优秀"
else:
    print "你要努力了！"

