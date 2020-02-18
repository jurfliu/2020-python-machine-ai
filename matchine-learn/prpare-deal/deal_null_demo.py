# -*- coding: utf-8 -*-

# @File    : deal_null_demo.py
# @Date    :  2020-02-18 16:25
# @Author  : admin
import pandas as pd
from sklearn.cluster import KMeans
#获取数据的null值
def p_max_min_null():
  datafile = '../data/air_data.csv'
  resultfile = 'tmp/explore.xls'
  data = pd.read_csv(datafile, encoding='utf-8')
  explore = data.describe(percentiles=[], include='all').T
  print(explore)
  print(explore['count'])
  #求空值数
  explore['null'] = len(data) - explore['count']
  print(explore['null'] )
  #截取部分列，组成子集
  explore = explore[['null', 'max', 'min']]
  print("===================================")
  print(explore)
  '''
  函数自动计算的字段有count（非空值数）、unique（唯一值数）、top（频数最高者）、
  freq（最高频数）、mean（平均值）、std（方差）、min（最小值）、50 %（中位数）、max（最大值）
  '''
  #获取数据的非0数据
def  p_not_0():
      datafile = '../data/air_data.csv'
      cleanedfile = 'tmp/data_cleaned.csv'
      data = pd.read_csv(datafile, encoding='utf-8')
      #截取显示的部分列
      #print(data[['GENDER',"WORK_PROVINCE"]]);

      #获取票价非零的，或者平均折扣率与总飞行公里数同时为0的记录；
      #1.先获取不为null的数据，在这里换做&运算
      data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]
      # 只保留票价非零的，或者平均折扣率与总飞行公里数同时为0的记录。
      #2.再获取不为0的数据
      index1 = data['SUM_YR_1'] != 0
      index2 = data['SUM_YR_2'] != 0
      index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0)  # 该规则是“与”
      data = data[index1 | index2 | index3]  # 该规则是“或”
      print(data)
#3.数据标准化
def  p_standard():
    datafile = '../data/zscoredata.xls'
    zscoredfile = 'tmp/zscoreddata.xls'
    data = pd.read_excel(datafile)
    # 核心语句，实现标准化变换，类似地可以实现任何想要的变换。
    #根据z-score（标准差）标准化公式zij＝（xij－xi）/si，其中zij是标准化后的变量值；
    # xij是实际变量值，xi为变量的算术平均值，si是变量的标准差，进行标准差标准化。
    data = (data - data.mean(axis=0)) / (data.std(axis=0))
    data.columns = ['Z' + i for i in data.columns]
    print(data);
    #data.to_excel(zscoredfile, index=False)





if __name__ == "__main__":
   # p_max_min_null();
   #p_not_0();
   p_standard();
   pass