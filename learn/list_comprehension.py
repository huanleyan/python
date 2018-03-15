#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

import time

#循环可以用来生成列表:
values = [2,2,3]
squares = []
for x in values:
    squares.append(x**2)
print(squares)

#列表推导式可以使用更简单的方法来创建这个列表
values = [3,8,10,14]
squares = [x ** 2 for x in values]
print(squares)   #[9, 64, 100, 196]

#可加入条件筛选，在上面的例子中，假如只想保留列表中不大于8的数的平方
squares = [x**2 for x in values if x<=10]
print(squares)  #[9, 64]

#平方的结果不大于100的
squares = [x**2 for x in values if x**2<=80]
print(squares)

#可以使用推导式生成集合和字典
values = [10, 21, 4, 7, 12]
square_set = {x**2 for x in values if x<=10}
print(square_set)  #{16, 49, 100}
squares_dict = {x: x**2 for x in values if x<=10}
print(squares_dict)  #{10: 100, 4: 16, 7: 49}

#计算上面例子中生成的列表中所有元素的和
total = sum([x**2 for x in values if x<=10])
print(total)   #165
#但是python会生成这个列表，然后放到垃圾回收机制中，这是一种浪费，因此使用产生表达式来解决
total = sum(x**2 for x in values if x<10)
print(total) #65
#与上面相比只是去掉了括号，但是并不会一次性的生成这个列表

#比较一下两者的用时
values = range(1000000)
t1 = time.time()
total = sum([x**2 for x in values if x<10])
print('list speed:', time.time()-t1)  #list speed: 0.04999995231628418

t2 = time.time()
total = sum(x**2 for x in values if x<10)
print('comprehension speed::',time.time()-t2)  #comprehension speed:: 0.0410001277923584
