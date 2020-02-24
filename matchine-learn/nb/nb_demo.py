# -*- coding: utf-8 -*-

# @File    : nb_demo.py
# @Date    :  2020-02-21 10:07
# @Author  : admin
from sklearn.datasets import fetch_20newsgroups, load_boston
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

'''
使用朴素贝叶斯进行分类
'''
def naviesbayes():
    #subset的值有all，train，test
    news_data=fetch_20newsgroups(subset='all');
    #获取分类类别
    print(list(news_data.target_names))
    #获取数据集文件的个数
    print(news_data.filenames.shape)
     #获取两篇数据
    print(list(news_data['data'][:2]))
    #获取指定类别中新闻的个数
    cat = ['alt.atheism']
    newsgroups_atheism = fetch_20newsgroups(subset='train', categories=cat)
    print(newsgroups_atheism.filenames.shape)
    #将文本转为TF-IDF向量
    #进行数据分割0.75:0.25
    x_train, x_test, y_train, y_test = train_test_split(news_data.data, news_data.target, test_size=0.25)
    # 对数据集进行特征抽取
    tf = TfidfVectorizer()
    # 以训练集当中的词的列表进行每篇文章重要性统计['a','b','c','d']
    x_train = tf.fit_transform(x_train)
    #提取的TF-IDF 向量是非常稀疏的，超过135000维的特征才有155个非零特征
    print(x_train.shape)
    #print(x_train.nnz / float(x_train.shape[0]))
    #print(tf.get_feature_names())
    # 进行朴素贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)
    print(x_train.toarray())
    mlt.fit(x_train, y_train)
    #使用测试集进行预测
    x_test = tf.transform(x_test)
    y_predict = mlt.predict(x_test)
    print("预测的文章类别为：", y_predict)
   # 得出准确率
    print("准确率为：", mlt.score(x_test, y_test))
    print("每个类别的精确率和召回率：", classification_report(y_test, y_predict, target_names=news_data.target_names))
   #指定数据集的预测

    return None

#调用执行
naviesbayes();