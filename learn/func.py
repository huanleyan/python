#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:chenghuan
'''
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

def add(a,b):
    c = a+b
    return c

#python 并没有限定参数的类型，因此可以使用不同的参数类型
print(add(2,3))  #5
print(add('foo', 'bar')) #foobar

#传入参数时python提供了两种选项
#第一种是上面使用的按照位置传入参数
#另一种是使用关键词模式，显式的指定参数的值
print(add(a=2, b=3))   #5
print(add(b='morning', a='good'))    #goodmorning  这个和php不太一样
print(add(2, b=3))    #5


#设定默认参数
def quad(x, a=1, b=0, c=0):
    return a*x*x*b*x+c

print(quad(2.0))   #0.0
print(quad(2.0, b=3))  #24.0   指定b=3


#接收不定参数
#使用如下方法，可以使用函数接受不定数目的参数，类似java的..多个参数
def add(x, *args):
    total = x
    for arg in args:
        total += arg
    return total
#*args表示参数数目不定，可以看成一个元组
#把第一个参数后面的参数当做元组中的元素
print(add(1,2,3,4,5)) #15
print(add(1,2))  #3


#使用关键词传入参数
def add(x, **kwargs):
    total = x
    for arg, val in kwargs.items():
        print("adding", arg)
        total += val
    return total

#**kwargs表示参数数目不定，相当于一个字典，关键词和值对应于键值对
print(add(1, a=2, b=3))
'''
adding a
adding b
6
'''

#可以接收任意数目的位置参数和键值对参数
def fun1(*args, **kwargs):
    print(args, kwargs)

fun1(4,5,a=11,b=12,c=13)    #(4, 5) {'c': 13, 'b': 12, 'a': 11}


#返回多个值，函数可以返回多个值
def to_val(x,y):
    r = (x**2 + y**2)**0.5
    total = x+y
    return r,total
a,b = to_val(3,4)
print(a,b)   ## 5.0    7

#事实上，python将返回的两个值变成了元组：
print(to_val(3,4))     #(5.0, 7)

#列表也有相似的功能，可以用来赋值
a,b,c = [1,2,3]
print(a,b,c)

#可以将参数用元组传入
def add(a,b):
    return a+b
c = (2,3)
## 这里的*必须要。
print(add(*c))   #5


#还可以用字典传入参数
d = {'a':'111','b':'222'}
## 这里的**必须要。
print(add(**d))   #7

#map方法生成序列
#map(func, aseq)
def fun_sqr(x):
    return x**2
a = [2,3,4]
print(map(fun_sqr, a))   #[4,9,16]

#事实上，根据函数参数的多少，map可以接受多组序列
#将其对应的元素作为参数传入函数
def add(a,b):
    return a+b
a = (2,3,4)
b = (10,11,15)
c = [7,8,9]
#a和b元素数目需要一致
x,y,z = map(add, a, b)
print(x)  #12
print(y)  #14
print(z)  #19
x1,y1,z1 = map(add, a, c)
print(x1)  #9
print(y1)  #11
print(z1)  #13



















#
