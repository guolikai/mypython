#!/usr/bin/env python

for i in range(1, 6):
    print '*' * i

for i in range(1, 6):
    for j in range(1, i + 1):
        print '*',
    print
