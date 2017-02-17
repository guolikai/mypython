#!/usr/bin/env python
#_*_ coding:utf8 _*_
import sys
sarlary = int(raw_input('请输入您计划购物的预算:'))
msg = '========shopping list========\nCar   50000\nIphone 4800\nBike    800\nCoffee   33\nRHCE   5980\n============================='
products = {'Car':50000,'Iphone':4800,'Bike':800,'Coffee':33,'RHCE':5980}
buy_count = 0
buy_list = []

while sarlary >= 0:
    print msg    
    buy = raw_input('您计划购买哪一种商品？')
    match_flag = False  #默认为False，如果用户购买成功，就设置为True
    if buy not in products.keys():
        print '您输入的信息不在购物车列表中，请重新选择：'
        continue
    elif buy in products.keys():
        voluse = products[buy]
        if voluse > sarlary:
            print '您现在剩下%s元，该商品不能购买。请重新选择：' % sarlary
            continue 
        match_flag = True
        buy_list.append(buy)
        sarlary -= voluse
        print '您已经购买了%s，花费金额%s元,您现在剩下%s元！' % (buy,voluse,sarlary) 
    if match_flag == True:
        buy_count += 1
    if sarlary <= 33:
        print '您的钱不可以再购买商品,系统将自动退出！'
        print '\033[31;1m您一共购买了%s次，商品依次是%s\033[0m' % (buy_count,buy_list)
        sys.exit()
    select = raw_input('请选择是否继续购买[y/n]:')
    if select == 'n':
        print '\033[31;1m您一共购买了%s次，商品依次是%s\033[0m' % (buy_count,buy_list)
        sys.exit('您选择退出购买。')
    elif select != 'y':
        print '选择输入有误，默认选是。请重新选择要购买的商品：'
        continue
