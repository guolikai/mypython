#!/usr/bin/env python
#_*_ coding:utf8 _*_

print_num = int(raw_input('Which loop  do you want it to be printed out!'))
count = 0

while count < 10000000:
    if count == print_num:
        print 'There you are the number:',count
        choice = raw_input('Do you want to continue the loop?(y/n)')
        if choice == 'n':
            break
        else:
            while print_num <= count:
                print_num = int(raw_input('Which loop  do you want it to be printed out!'))
                print 'count 已经过了'
    else:
        print 'Loop:',count 
    count += 1
else:
    print 'Loop:',count 
