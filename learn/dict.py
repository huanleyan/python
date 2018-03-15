#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
author  chenghuan
'''
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

import pprint
#字典dictionary,在一些编程语言中也称谓hash, map
#是一种由键值对组成的数据结构
a = {}
print(type(a))   #<class 'dict'>
a = dict()
print(type(a))   #<class 'dict'>

#插入键值
a['c'] = 'cheng'
a['h'] = 'huan'
print(a)  #{'h': 'huan', 'c': 'cheng'}

#查看键值
print(a['c'])  #cheng

#更新
a['c'] = 'li'
print(a)   #{'h': 'huan', 'c': 'li'}

#初始化字典
a = {'first':'num1', 'second':'num2', '3':'num3'}
print(a['first'])  #num1
# Python中不能用支持用数字索引按顺序查看字典中的值，
# 而且数字本身也有可能成为键值，这样会引起混淆:
# a[3] 会报错
#print(a[3])  #KeyError: 3




#------------例子-----------
e1 = {'mag': 0.05, 'width': 20}
e2 = {'mag': 0.04, 'width': 25}
e3 = {'mag': 0.05, 'width': 80}
e4 = {'mag': 0.03, 'width': 30}
# 以字典作为值传入新的字典
events = {500: e1, 760: e2, 3001: e3, 4180: e4}
print(events)   #{760: {'width': 25, 'mag': 0.04}, 3001: {'width': 80, 'mag': 0.05}, 500: {'width': 20, 'mag': 0.05}, 4180: {'width': 30, 'mag': 0.03}}

#------------另一个例子-------------
people = [
    {'first': 'Sam', 'last': 'Malone', 'name': 35},
    {'first': 'Woody', 'last': 'Boyd', 'name': 21},
    {'first': 'Norm', 'last': 'Peterson', 'name': 34},
    {'first': 'Diane', 'last': 'Chambers', 'name': 33}
]
print(people[0])    #{'name': 35, 'first': 'Sam', 'last': 'Malone'}

#使用dict初始化字典
#除了通常的定义方式，还可以通过dict转化来生成字典
my_dict = dict([('name','chenghuan'),('age',28),('sex','female')])
print(my_dict)     #{'age': '28', 'name': 'chenghuan', 'sex': 'female'}

#利用索引直接更新键值对
my_dict['age'] += 1
print(my_dict)    #{'name': 'chenghuan', 'age': 29, 'sex': 'female'}

#可以使用元组作为键值
#例如，可以利用元组做键来表示从第一个城市飞往第二个城市的航班数的多少
channel = {}
channel[('shanghai','zhengzhou')] = 100
channel[('zhengzhou', 'shanghai')] = 101
channel[('zhengzhou','nanyang')] = 55
channel[('xinyang', 'nanyang')] = 44
#元组是有序的，因此('shanghai','zhengzhou')和('zhengzhou', 'shanghai')是两个不同的键
print(channel[('shanghai','zhengzhou')])   #100
print(channel[('zhengzhou', 'shanghai')])   #101

#字典方法
#get方法:d.get(key, default=None)
# get 返回字典中键 key 对应的值，
# 如果没有这个键，返回 default 指定的值（默认是 None ）
a = {'first':'num1', 'second':'num2'}
#print(a['third'])   #KeyError: 'third'
print(a.get('third',None))   #None

#pop方法删除元素，弹出字典中某个键对应的值，同事可以指定默认参数
#d.pop(key, default=None)
c = a.pop('first')
d = a.pop('third','third not exist')
print(c)    #num1
print(d)    #third not exist
print(a)    #{'second': 'num2'}

#和列表类似，del函数可以删除字段中特定的键值对，例如:
a = {'first':'num1', 'second':'num2'}
del a['first']
# 删除的key不存在报错    del a['third']  #KeyError: 'third'
print(a) #{'second': 'num2'}

#update方法可以更新字典
#可以通过索引插入或删除字典中特定的键值对
my_dict = dict([('name', 'chenghuan'),('sex','nan'),('age',28)])
dict_update = {'name':'lidan','marriage':'single'}
my_dict.update(dict_update)
print(my_dict)  #{'age': 28, 'name': 'lidan', 'marriage': 'single', 'sex': 'nan'}

#in 查询字典中是否有该键值
dict_123 = {'age': 28, 'name': 'lidan', 'marriage': 'single', 'sex': 'nan'}
print('name' in dict_123)    #True
print('address' in dict_123) #False
#keys()方法返回字典中所有的key
print(dict_123.keys())  #dict_keys(['age', 'marriage', 'sex', 'name'])
#values(）方法返回字典中所有值组成的列表)
print(dict_123.values()) #dict_values([28, 'single', 'nan', 'lidan'])
#items()返回所有键值对元组组成的列表
print(dict_123.items())#dict_items([('age', 28), ('marriage', 'single'), ('sex', 'nan'), ('name', 'lidan')])

for k,v in dict_123.items():
    print(k,v)
'''
age 28
marriage single
name lidan
sex nan
'''
