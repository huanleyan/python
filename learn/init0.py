#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

'''
@description: 特殊方法
@author:chenghuan
'''
# 特殊方法
# Python 使用 __ 开头的名字来定义特殊的方法和属性，它们有：
#
# __init__()
# __repr__()
# __str__()
# __call__()
# __iter__()
# __add__()
# __sub__()
# __mul__()
# __rmul__()
# __class__
# __name__

#构造方法  __init__()
#在产生对象之前，我们可以向对象中添加属性
#还可以通过构造方法，在构造对象的时候直接添加属性
class Clothes(object):
    def __init__(self, name='chenghuan'):
        self.c_name = name
my_cloth = Clothes()
print(my_cloth.c_name)

#传入有参数的值
you_cloth = Clothes('lidan')
print(you_cloth.c_name)

#表示方法__repr__() 和__str__()
class People(object):
    def __init__(self, name='chenghuan'):
        self.c_name = name
    def __str__(self):
        return ("a{} clothes".format(self.c_name))
    def __repr__(self):
        return ("{}(color='{}')".format(self.__class__.__name__, self.c_name))

#__str__()是使用print函数显示的结果，类似于java的toString
my_people = People()
print(my_people)

#__repr__()返回的是不适用print方法的结果
print(my_people.__class__, my_people.__class__.__name__, my_people.color) 
