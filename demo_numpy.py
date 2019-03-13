#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2019-03-12 Guolikai
# 功能: 使用科学计算库NumPy简化程序
from matplotlib import pyplot as plt
import numpy as np


# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def demo():
    # 生成1-99数组
    arr_1 = np.arange(1,100)
    print(arr_1)
    # s生成随机数是2-12的20列10行矩阵
    arr = np.random.randint(2,13,(10,20))
    print(arr)

    # 改变数组形状
    arr1 = np.reshape(arr,(8,25))
    print(arr1)


def main():
    """
       直方图绘制: plt.hist(data,bins)   data,数据列表；bins：分组边界
        edgecolor:    边界颜色
        linewidth:    边界线宽度
        rwidth:       直方图宽度
        density:      概率统计(老版本normed)
    """
    total_num = 10000
    arr_a = np.random.randint(1, 7, total_num)
    arr_b = np.random.randint(1, 7, total_num)
    # numpy数据运算，即向量化运算
    arr = arr_a  + arr_b
    # print('第一个数组:{}'.format(arr_a))
    # print('第二个数组:{}'.format(arr_b))
    # print('二个数组和:{}'.format(arr))
    # print('二个数组相乘:{}'.format(arr_a * arr_b))

    # 直接生产直方图的统计具体数据
    hist, bins = np.histogram(arr,bins=range(2, 14))
    print(hist)
    print(bins)
    # 数据可视化
    # X轴加单位,设置x轴坐标点显示
    tick_labels = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5   #生成位置并修改
    plt.xticks(tick_pos, tick_labels)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('统计数量')
    plt.hist(arr, bins=range(2, 14),  density=0, edgecolor='black', linewidth=1, rwidth=0.8)
    plt.show()


if __name__ == '__main__':
    demo()
    # main()
