#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

#列表是可变的(Mutable)
a = [1,2,4,5]
a[0] = 100
a.insert(3,200)
print(a)   #[100, 2, 4, 200, 5]
a.insert(10,200)
print(a)   #[100, 2, 4, 200, 5, 200]


#字符串是不可变的（Immutable）
s = 'hello world'
#通过索引改变会报错，例如 s[0] = c

#字符串方法只是返回一个新的字符串，并不改变原来的值
print(s.replace('world', 'Mars')) #hello Mars
print(s)  #hello world

#如果想改变字符串的值，可以用重新赋值的方法
s = s.replace('world', 'YunNan')
print(s)

#可变数据类型：list, dictionary,set,numpy,array, user defined object
#不可变数据类型：integer, float, long, complex, string, tuple, fozenset
