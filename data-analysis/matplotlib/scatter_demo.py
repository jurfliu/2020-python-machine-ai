# -*- coding: utf-8 -*-

# @File    : scatter_demo.py
# @Date    :  2020-02-18 15:38
# @Author  : admin

# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager
#x,y轴
x_1=range(1,32);
x_2=range(51,82);
y_1=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23];
y_2=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6];
#windows下设置字体
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#设置图形大小
plt.figure(figsize=(10,8),dpi=80)
#使用scatter方法绘制散点图,和之前绘制折线图的唯一区别
plt.scatter(x_1,y_1,label="1月份");
plt.scatter(x_2,y_2,label="2月份")

#调整x轴的刻度
x_=list(x_1)+list(x_2);#转换成
x_tick_labels=["1月份{}日".format(i) for i in x_1];
x_tick_labels=x_tick_labels+["2月{}日".format(i-50) for i in x_2]
#x轴的标签要和x轴的数据对应,[::3]表示：从开始到结束，步长为3；
plt.yticks(y_1[::3],y_2[::3])
#添加图例
plt.legend(loc="upper left")
#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("标题")
#展示
plt.show()
