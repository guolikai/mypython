#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2019-03-12 Guolikai
# 功能: 图形绘制matplotlib模块学习


from matplotlib import pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def pyplot_scatter_demo():
    print('散点图绘制演示')
    x = [1,2,3,4,5,6,7,8,9]
    y = [1,2,3,4,5,6,7,8,9]
    # x, y分别是x坐标和y坐标的列表
    plt.scatter(x, y)

    plt.title('图形绘制matplotlib模块学习')
    # 设置坐标轴的标签
    plt.xlabel('X轴'), plt.ylabel('Y轴')
    plt.show()


def pyplot_hist_num_demo():
    """ 直方图绘制
        #plt.hist(data,bins)   data,数据列表；bins：分组边界
    """
    print('直方图绘制演示')
    roll_list = [2,3,4,5,6,6,6,6,7,8,9,10,11,12,3]
    # 数量统计
    plt.hist(roll_list, bins=range(2, 13),edgecolor='black',linewidth=1,rwidth=0.8)
    # 出现频率统计
    # plt.hist(roll_list, bins=range(2, 13), density=1, edgecolor='black', linewidth=1,rwidth=0.8)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('数量')
    plt.show()


def pyplot_hist_rate_demo():
    """ 直方图绘制: plt.hist(data,bins)   data,数据列表；bins：分组边界
        edgecolor:    边界颜色
        linewidth:    边界线宽度
        rwidth:       直方图宽度
        density:      概率统计(老版本normed)
    """
    print('直方图绘制演示')
    roll_list = [2,3,4,5,6,6,6,6,7,8,9,10,11,12,3]
    # 数量统计
    # plt.hist(roll_list, bins=range(2, 13),edgecolor='black',linewidth=1,rwidth=0.8)
    # 频率统计参数 density=1  老版本normed=1
    plt.hist(roll_list, bins=range(2, 13), density=1, edgecolor='black', linewidth=1,rwidth=0.8)
    plt.title('骰子投掷频率统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()

if __name__ == '__main__':
    # pyplot_scatter_demo()
    # pyplot_hist_num_demo()
    pyplot_hist_rate_demo()
