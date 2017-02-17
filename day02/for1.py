#!/usr/bin/env python

alist = [10, 20, 'tom']

for item in alist:
    print item

for ind in range(len(alist)):
    print "%s:%s" % (ind, alist[ind])
