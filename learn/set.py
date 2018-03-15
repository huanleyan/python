#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
集合的操作方法
'''
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

#列表和字符串都是一种有序序列，而集合set是一种无序的序列
#因为集合是无序的，当集合中存在两个相同元素的时候，只会保存其中的一个（唯一性）
#同时为了确保其中不包含同样的元素，集合中放入的元素只能是不可变的对象（确定性）

#可以用set()函数生成空集合
a = set()
print(type(a))

#使用列表来初始化一个集合
a = set([1,2,3,4,1])
print(a)  #{1, 2, 3, 4}   ,自动去除重复元素1

#集合中的元素是通过大括号{}包含起来的，可以用{}的形式创建集合
a = {1,2,3,4,5,1}
print(a)   #{1, 2, 3, 4, 5}

#但是创建空集合的时候只能用set来创建，因为在python中{}创建的是一个空的字典
s = {}
print(type(s))  #<class 'dict'> 创建的是一个空的字典而不是一个集合

#集合操作
x = {1,2,3,4}
y = {2,3,4,5}
z = {1,2}
#求并集
#可以用方法a.union(b) 或者操作 a|b实现
c = x.union(y)
d = x|y
print(c)  #{1, 2, 3, 4, 5}
print(d)  #{1, 2, 3, 4, 5}

#求交集
#可以用a.intersection(b) 或者 a&b实现
c1 = x.intersection(y)
d1 = x & y
print(c1) #{2, 3, 4}
print(d1) #{2, 3, 4}

#求差集
#a和b的差集，返回只在a不在b的元素组成的集
#可以用方法a.difference(b)或者操作a-b实现
c2 = x.difference(y)
d2 = x - y
print(c2)  #{1}
print(d2)  #{1}

#对称差
#a和b的堆成差集，返回在a或者b中，但不同时在a和b中的元素组成的集合
#可以用方法 a.symmetric_difference(b) 或者a^b实现（异或操作符）
c3 = x.symmetric_difference(y)
d3 = x^y
print(c3)  #{1, 5}
print(d3)   #{1, 5}

#包含关系（子集）
#要判断b是不是a的子集，可以用、b.issubset(a)方法或者更简单的 b<=a
c4 = z.issubset(x)
d4 = (z<=x)
print(c4)  #True
print(d4)  #True
#方法只能用来测试子集，但是操作符可以用来判断真子集
print(z<x) #True
print(z<=x) #True

#---------------集合方法---------------------------
#add方法向集合中添加元素，类似列表中的append方法，向集合中添加单个元素
x.add(10)
print(x)   #{1, 2, 3, 4, 10}

#update方法向集合中添加多个元素
x.update([11,12,13])
print(x)  #{1, 2, 3, 4, 10, 11, 12, 13}

#remove方法移除单个元素
x.remove(10)
print(x) #{1, 2, 3, 4, 11, 12, 13}

#pop方法弹出元素
#由于集合没有顺序，不能像列表一样按照位置弹出元素
#pop方法删除并返回集合中任意一个元素，如果集合中没有元素会报错
s = {1,4,7}
d = s.pop()
print(s,d)

#discard方法作用和remove一样
s = {1,4,7}
s.discard(3)
print(s)   #set([1,4])

#difference_update方法
#a.difference_update(b)从a中去除所有属于b的元素
a = {1,2,3,4}
b = {2,3,4,5}
a.difference_update(b)
print(a) 
