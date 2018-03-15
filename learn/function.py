#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

#在python中，函数是一种基本类型的对象，所以
#1.可以将函数作为参数传递给另一个函数
#2.将函数作为字典的值储存
#3.将函数作为另一个函数的返回值
def square(x):
    return x*x

def cube(x):
    return x*x*x

#函数的基本类型
#函数可以作为字典值存储
funcs = {'square':square, 'cube':cube}
print(funcs)  #{'square': <function square at 0x000000000210CBF8>, 'cube': <function cube at 0x000000000220DAE8>}
x = 2
for func in sorted(funcs):
    print(func, funcs[func](x))
'''
cube 8
square 4
'''

#函数参数，引用传递
#传递给函数f的是指向x所包含的内容的引用，，
#如果我们修改了指向内容的值(x[0]='wangdawei')，那么外面的x的值也会被改变
#这点和php不太一样
def mod_f(x):
    x[0] = 'wangdawei'
    return x
x = ['chenghuan','chengyan','chengaaa']
print(x)
print(mod_f(x))
print(x)
'''
['chenghuan', 'chengyan', 'chengaaa']
['wangdawei', 'chengyan', 'chengaaa']
['wangdawei', 'chengyan', 'chengaaa']
'''

#如果我们在函数中赋给x一个新的值（例如另一个列表）
#那么在函数外面的x值不会改变
def no_mod_f(x):
    x = [4,5,6]
    return x
x = [1,2,3]
print(x)
print(no_mod_f(x))
print(x)
'''
[1, 2, 3]
[4, 5, 6]
[1, 2, 3]
'''

#高阶函数
#以函数作为参数，或者返回一个函数的函数是高阶函数
#常用的例子有map和filter函数
#map(f,sq)函数，将f作用到sq的每个元素上面去，并返回组成的列表
#相当于
#[f(s) for s in sq]
squ = list(map(square, range(5)))
print(squ)  #[0, 1, 4, 9, 16]

def is_even(x):
    return x%2 == 0
even_a = filter(is_even,range(5))
print(list(even_a))  #[0,2,4]
even_b = map(square, filter(is_even, range(5)))
print(list(even_b))  #[0, 4, 16]

#返回一个函数
def get_logger_func(target):
    def write_logger(data):
        with open(target, 'a') as f:
            f.write(data + '\n')
    return write_logger

fun_logger = get_logger_func('chenghuan.txt')
fun_logger('ming tian hui geng hao')

#匿名函数lambda
print(map(square, range(5)))
#用匿名函数替换为：
print(map(lambda x :x*x , range(5)))

#简单的写法
s2 = sum(x**2 for x in range(1,3))
print(s2)   #5

#global变量
#要在函数中修改全局变量的值，需要加上global关键字
x=15
def print_new():
    global x
    x = 18
    print(x)
print_new()   #18
print(x)    #18


#递归
#一般对于分治法，要用递归，不过在python中不怎么用
#更高效的处理
def fib(n):
    a,b = 0,1
    for i in range(1,n+1):
        a,b = b, a+b
    return b


















#
