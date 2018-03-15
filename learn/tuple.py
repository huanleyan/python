#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
介绍列表的方法及示例演示其作用，包括:长度、修改列表、取值、排序
'''
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

#与列表相似，元祖Tuple也是个有序序列，但是元组是不可变的，用（）生成
a = (10, 11, 12, 13, 15)
print(a)

#可以索引切片
c = a[1]
print(c) #11

d = a[1:3]
print(d) #(11,12)

#单个元素的元组生成
#采用下列方式定义只有一个元素的元组
e = (10,)
print(e)  #(10,)
print(type(a))  #<class 'tuple'>

#tuple(lst) 列表转元组
f = [11,22,33,44]
f_a = tuple(f)
print(f_a)

#由于元组是不可变的，所以只能有一些不可变的方法
#例如计算元素个数count和元素位置index,用法与列表一样
f1 = f.count(11)
print(f1) #1

fb = f.index(33)
print(fb)  #2
