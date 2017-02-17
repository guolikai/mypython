#!/usr/bin/env python
f = file('/etc/passwd','r')

for line in f.readlines():
    #print line,
    #print line.split(':')
    print line.strip('\n').split(':')[0]  #cat /etc/passwd | awk -F: '{print $1}'
