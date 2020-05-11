#!usr/bin/env python
#-*- coding:utf-8 _*-
'''
@author:Administrator
@file: knn.py
@time: 2020-02-23 上午 11:12
https://www.cnblogs.com/bigox/p/11476948.html  最后有说明怎么保存模型
'''
import pandas as pd

#knn预测用户签到位置
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def knn_demo():
    #1.加载读取数据
    data=pd.read_csv("../data/knn-dataset.csv")
    #打印数据
    #print(data.head(10));
    ############2.处理数据##########
    # 2.1缩小数据,查找指定范围数据
    data = data.query("x > 0.2 &  x < 10.25 & y > 1.5 & y < 10.75")
    # 2.2处理时间的数据
    time_value = pd.to_datetime(data['time'], unit='s')
    # 2.3把日期格式转换成 字典格式
    time_value = pd.DatetimeIndex(time_value)
    print(time_value)
    # 构造一些特征,使用 DafaFrameming.loc[行名, 列名] = 值 的方式去赋值, 而不是使用DataFrame[][]的形式去赋值.
    #给数据构建新的列的话，需要先复制一份副本数据，在副本数据上构建，不然会报过时等问题
    temp_data = data.copy();
    temp_data.loc[:,('day')] = time_value.day
    temp_data.loc[:,('hour')] = time_value.hour
    temp_data.loc[:,('weekday')] = time_value.weekday
    print(temp_data)
    # 把原来的时间戳特征列删除
    temp_data = temp_data.drop(['time'], axis=1);
    # 把签到数量少于n个目标位置删除
    place_count = temp_data.groupby('place_id').count()
    print(place_count)
    tf = place_count[place_count.row_id > 1].reset_index()
    cofirmed_data=temp_data[temp_data['place_id'].isin(tf['place_id'])];
    print(cofirmed_data)
    #获取特征值和目标值
    #方法一
    x_feacture = cofirmed_data[['row_id', 'x', 'y', 'accuracy']]
    y_target = cofirmed_data[['place_id']]
    print(x_feacture,y_target)
    #方法二
    y = cofirmed_data['place_id']
    x = cofirmed_data.drop(['place_id'], axis=1)
    #print("获取特征值，目标值方法二:")
    #print(x,y)
    # 进行数据的分割训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    print("训练集:",x_train)
    print("测试集:",x_test)
    #特征工程标准化
    std = StandardScaler()
    # 对测试集和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)
    # 进行算法流程 # 超参数
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(x_train, y_train)
    #得出预测结果
    y_predict = knn.predict(x_test)
    print("预测的目标签到位置为：", y_predict)
    # 得出准确率
    print("预测的准确率:", knn.score(x_test, y_test))
   # print(classification_report(y_test,y_predict))

    #保存模型
    from sklearn.externals import joblib
    # 保存
    joblib.dump(knn, '../data/knn.m')
    # 提取算法
    knn_digits = joblib.load('../data/knn.m')
    # 使用模型
    y_p = knn_digits.predict(x_test)
    print(y_p)
    return None


def testmodel():
    from sklearn.externals import joblib
    data = pd.read_csv("../data/knn_data.csv")
    data=data.head(1);
    print(data)

    # 特征工程标准化
    std = StandardScaler()
    # 对测试集和训练集的特征值进行标准化
    x_test = std.fit_transform(data)
    print(x_test)
    # 提取算法
    knn_digits = joblib.load('../data/knn.m')
    # 使用模型
    y_p = knn_digits.predict(x_test)
    print(y_p)




#knn_demo();
if __name__ =="__main__":
  knn_demo();
 #testmodel();




