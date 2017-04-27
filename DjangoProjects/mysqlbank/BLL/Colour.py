#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
'''{30:黑色,31:红色,32:绿色,33:黃色,34:蓝色,35:紫红色,36:青蓝色,37:白色} '''
class Colour(object):
    def __init__(self):
        pass
    def black(self,info):            #定义黑色闪烁字体
        print '\033[30;5m %s \033[0m' %  (info)
    def red(self,info):              # 定义红色闪烁字体
        print '\033[31;5m %s \033[0m' % (info)
    def green(self,info):            # 定义绿色闪烁字体
       print '\033[32;5m %s \033[0m' % (info)
    def yellow(self,info):           # 定义黃色字体
        print '\033[33;5m %s \033[0m' % (info)
    def purple_red(self,info):       # 定义紫红色字体
        print '\033[35;5m %s \033[0m' % (info)
    def blue(self,info):             # 定义蓝色字体
        print '\033[36;5m %s \033[0m' % (info)
    def white(self,info):            # 定义白色字体
        print '\033[37;5m %s \033[0m' % (info)
