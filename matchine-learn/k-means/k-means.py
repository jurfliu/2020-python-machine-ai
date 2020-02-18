# -*- coding: utf-8 -*-

# @File    : k-means.py
# @Date    :  2020-02-18 9:58
# @Author  : admin
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#参数初始化
inputfile = '../data/consumption_data.xls' #销量及其他属性数据
k = 3 #聚类的类别
iteration = 500 #聚类最大循环次数
#1.读取数据
data = pd.read_excel(inputfile, index_col = 'Id')
print("读取原始数据：",data);
#2.数据标准化 使用规范化方法
data_zs = 1.0*(data - data.mean())/data.std() #数据标准化 使用规范化方法       https://blog.csdn.net/bbbeoy/article/details/70185798
print("========data-zs 标准化后：========:",data_zs);
#3.开始聚类
model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration) #分为k类，并发数4
model.fit(data_zs) #开始聚类
#4.查看每个点预测的聚类
y=model.predict(data_zs);
print(y)
print(model.labels_)
#5.统计各个类别的数目
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
print("统计各个类别的数目",r1);
print(model.cluster_centers_)
#6.找出聚类中心
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
#7.横向连接（axis=0是纵向），中心点-类别数目
r = pd.concat([r2, r1], axis = 1) #横向连接（axis=0是纵向），得到聚类中心对应的类别下的数目
#8.重新设置pd的列名称
r.columns = list(data.columns) + [u'类别个数'] #重命名表头
#9.详细输出原始数据及其类别，主要concat函数的引用，原始数据-类别数目
r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)  #详细输出每个样本对应的类别
r.columns = list(data.columns) + [u'聚类后类别'] #重命名表头
# matplotlib 可视化显示
def density_plot(data):  # 自定义作图函数
    global k
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    ##subplots = True制作子图 sharex = False是不共享X轴刻度
    p = data.plot(kind='kde', linewidth=2, subplots=True, sharex=False)
    [p[i].set_ylabel(u'密度') for i in range(k)]
    plt.legend() #加不加这句代码都不影响
    return plt
pic_output = 'e:/'  # 概率密度图文件名前缀
for i in range(k):
      density_plot(data[r[u'聚类后类别'] == i]).savefig(u'%s%s.png' % (pic_output, i))