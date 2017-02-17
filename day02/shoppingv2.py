#!/usr/bin/env python
#_*_ coding:utf8 _*_
import sys

sarlary = int(raw_input('请输入您计划购物的预算:'))
products = [50000,4800,800,33,5980]
shopping_list=['Car','Iphone','Bike','Coffee','RHCE']
buy_count = 0
buy_list = []
msg = '''========shopping list========
(0) Car   50000
(1) Iphone 4800
(2) Bike    800
(3) Coffee   33
(4) RHCE   5980
=============================
您计划购买哪一种商品(0/1/2/3/4)？'''

while sarlary >= 0:
    buy = int(raw_input(msg))
    match_flag = False  #默认为False，如果用户购买成功，就设置为True
    if buy not in range(5):
        print '您输入的信息不在购物车列表中，请重新选择：'
        continue
    voluse = products[buy]
    if voluse > sarlary:
        print '您现在剩下%s元，该商品不能购买。请重新选择：' % sarlary
        continue 
    if voluse <= sarlary:
        match_flag = True
        buy_list.append(shopping_list[buy])
        sarlary -= voluse
        print '您已经购买了%s，花费金额%s元,您现在剩下%s元！' % (shopping_list[buy],voluse,sarlary) 
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
