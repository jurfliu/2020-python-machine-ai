# -*- coding: utf-8 -*-

# @File    : zhexian_demo2.py
# @Date    :  2020-02-24 10:28
# @Author  : admin
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#windows中的解决办法
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示
file_data=pd.read_excel("../data/train.xlsx");
#print(file_data);
print(type(file_data))
file_data=file_data.head(23)
print(file_data)
x=file_data['日期'];
y1=file_data['合同应收金额'];
y2=file_data['合同实收金额'];
print(type(x))
print(type(y1))
#x,y不能为dataframe格式，如：y=file_data[:,[4]]获取的是dataframe格式，传入plot方法中报错
#单独获取某一列为Series
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y1, label="合同应收金额", color="green")
plt.plot(x, y2, label="合同实收金额", color="orange")
# 添加图例
plt.legend(loc="upper left")
#添加
plt.xticks(range(len(x)),x,rotation=45)
#添加描述信息
plt.xlabel("时间")
plt.ylabel("金额 单位(人民币)")
plt.title("people go 2月份营收金额情况")
# 展示
plt.show()

