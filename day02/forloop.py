#!/usr/bin/env python

name = ['glk','wdx','per',1,2,3,5,4,'glk','wdx',1,2,3,4,5,6]

first_pos = 0
#for i in range(name.count(2)):
#    new_list = name[first_pos:]
#    next_pos = new_list.index(2) +1 
#    print 'Find postion:', first_pos + new_list.index(2)
#    first_pos += next_pos
for i in range(name.count(2)):
    if first_pos == 0:
        first_pos = name.index(2)
    else:
        first_pos = name.index(2,first_pos+1)
    print 'Find postion:',first_pos
