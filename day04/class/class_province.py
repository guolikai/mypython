#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-8 @Author:Guolikai'''

class Province:                         #定义类
    Message = '中国的23个省之一'       #属于类的属性；静态字段
    def __init__(self,name,capital):    #定义对象，self相当于类的封装；对象方法
        self.Name = name                #属于对象的属性；动态字段
        self.Capital = capital
    def sports_meet(self):              #对象动态方法
        return self.Name + '正在开运动会'
    @staticmethod                       #调用Python自带的装饰器，
    def fangfu():                       #类静态方法;数据库处理
        return '每个省都在反腐！'
    @property                           #类的特性，改变方法的访问形式：字段
    def bar(self):
        print self.Name
if __name__ == '__main__':
    hn = Province('河南','郑州')
    hb = Province('河北','石家庄')
    print Province.Message   #静态类不能访问动态字段，动态对象可以访问静态字段；建议不用
    print hn.Message,hn.Name,hn.Capital
    print hn.sports_meet()
    print hb.sports_meet()
    print Province.fangfu()
    hn.bar                                #加()报错
