# -*- coding: utf-8 -*-

# @File    : test.py
# @Date    :  2020-02-21 16:24
# @Author  : admin
a={1,2,4,5,7};
b={4,3,8,34}
print(a.union(b))   #并集
print(a | b)


postingList = [['my','dog','has','flea','problems','help','please'],
                 ['maybe','not','take','him','to','dog','park','stupid'],
                   ['my','dalmation','is','so','cute','I','love','him'],
                  ['stop','posting','stupid','worthless','garbage'],
                   ['mr','licks','ate','my','steak','how','to','stop','him'],
                   ['quit','buying','worthless','dog','food','stupid']]
returnVec = [0]*len(postingList)
print(returnVec);