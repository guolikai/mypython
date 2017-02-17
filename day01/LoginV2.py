#!/usr/bin/env python
#_*_ coding:utf8 _*_
import sys
retry_limit = 3
retry_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'
while retry_count < retry_limit:  #只要重试不超过3次就不断循环
    username = raw_input ('\033[32;1mUsername:\033[0m')
    lock_check = file(lock_file) #当用户输入用户名后，打开LOCK文件以检查用户是否LOCK了
    for line in lock_check.readlines():    #循环LOCK文件
        line = line.split()
        if username == line[0]:
            sys.exit('\033[31;1mUser %s is locked!\033[0m' % username)  #如果LOCK了就直接退出;跳出整个程序
    password = raw_input ('\033[32;1mPassword:\033[0m')
    f = file(account_file,'rb')   #打开账号文件
    match_flag = False #默认为False，如果用户match上了，就设置为True
    for line in f.readlines():
        user,passwd = line.strip('\n').split()
#去掉多余的\n并把这一行按空格分成2列，分别赋值为user，passwd两个变量
        if username == user and password ==passwd:  #判断用户名和密码是否都相等
            print 'Match!',username 
            match_flag = True   #相等就把循环外的match_flag变量改为True
            break   #跳出循环，因为已经match上了
    f.close()
    if match_flag == False:  #如果match_flag还是False，说明上面循环没match用户名密码，要继续循环
        print 'Username unmatched!'
        retry_count += 1
    else:
        print 'Welcome login Linux_Python!'   
        break    
else:
    print 'Your acount is locked!'
    f = file(lock_file,'ab')
    f.write(username,)
    f.close()

  
