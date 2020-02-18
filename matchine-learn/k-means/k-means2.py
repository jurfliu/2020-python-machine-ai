# -*- coding: utf-8 -*-

# @File    : k-means2.py
# @Date    :  2020-02-18 11:25
# @Author  : admin
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def programmer_4():
    inputfile = '../data/zscoreddata.xls'
    k = 5
    data = pd.read_excel(inputfile)
    kmodel = KMeans(n_clusters=k, n_jobs=4)
    kmodel.fit(data)
    r1 = pd.Series(kmodel.labels_).value_counts()  # 统计各个类别的数目
    r2 = pd.DataFrame(kmodel.cluster_centers_)  # 找出聚类中心
    r = pd.concat([r2, r1], axis=1)  # 横向连接（axis=0是纵向），得到聚类中心对应的类别下的数目
    r.columns = list(data.columns) + [u'类别个数']  # 重命名表头
    print(r)
    #matlib 显示
    import matplotlib.pyplot as plt
    plt.figure(figsize=(5,5));
    colored = ["orange", "green", "blue","red","yellow"];
    colr = [colored[i] for i in kmodel.labels_];
    plt.scatter(data.values[:, 0], data.values[:, 1], color=colr);
    plt.show()
programmer_4();