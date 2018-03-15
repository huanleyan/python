#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
介绍列表的方法及示例演示其作用，包括:长度、修改列表、取值、排序
'''
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

empty_list =list()
print(empty_list) #[]

#用len查看列表长度
a = [1, 2, 3]
b = [4, 5, 'hello']
c = a + b
print(c) #[1, 2, 3, 4, 5, 'hello']

d = b * 2
print(d) #[4, 5, 'hello', 4, 5, 'hello']

print(d[-1])  #hello

print(a) #[1,2,3]
#修改列表
a[0] = 110
print(a)  #(110, 2, 3)

#下面这种赋值也适用于分片，将列表的2,3两个元素换掉
a[1:3] = [210, 310]
print(a)  #[110, 210, 310]

#事实上，对于连续的分片（即步长为 1 ），Python采用的是整段替换的方法，
# 两者的元素个数并不需要相同，
a[1:3] = [210, 310, 410, 510, 511] #[110, 210, 310, 410, 510, 511]
print(a)

#删除列表中一个连续的分片
a[1:3] = []
print(a)  #[110, 410, 510, 511]

#对于不连续，间隔step不为1 的片段进行修改时，两者元素数目必须一致
#a[::2] = [22, 33, 44] #ValueError: attempt to assign sequence of size 3 to extended slice of size 2
a[::2] = [22, 33]
print(a)  #[22, 410, 33, 511]

#使用del方法删除列表中的元素
del(a[0])
print(a) #[410, 33, 511]

#del a[::2]   删除间隔的元素

#用in判断某个元素是否在某个序列(不仅仅是列表)中
#用、not in 来判断是否不在某个序列中
print(33 in a) # True
print(1 not in a) #True


#也可以作用于字符串
s = 'hello world'
print('he' in s)   #True
print('world' not in s)   #False

#列表中可以包含各种对象，甚至可以包含列表
c = [1, 2, 'six', [3,4]]
print(c[2])   #six
print(c[3][1]) #4


#----------------列表方法---------------
#列表中元素个数
t = [11, 22, 33,11, 44, 55, 66]
print(len(t))   #6

#元素11出现的个数
print(t.count(11)) #2

#li.index(ob) 返回元素中ob第一次出现的索引位置，如果ob不在li中会报错
print(t.index(44))  #4


#向列表中添加单个元素
#li.append(ob)将元素ob添加到li的最后
t.append(77)
print(t)   #[11, 22, 33, 11, 44, 55, 66, 77]

# append每次只添加一个元素，并不会因为这个元素是序列而将其展开：
t.append([88,99,100])  #[11, 22, 33, 11, 44, 55, 66, 77, [88, 99, 100]]
print(t) #

#向列表中添加序列
#li.extend(lst) 讲序列lst中的元素依次添加到列表li的最后，作用相当于li+=lst
t.extend([111,122,133]) #[11, 22, 33, 11, 44, 55, 66, 77, [88, 99, 100], 111, 122, 133]
print(t)

#向列表中插入元素
#li.insert(idx, ob)在索引idx处插入ob，之后的元素依次后移
t.insert(1,'a')
print(t)  #[11, 'a', 22, 33, 11, 44, 55, 66, 77, [88, 99, 100], 111, 122, 133]

#移除元素
#li.remove(ob) 会将列表中第一个出现的ob删除，如果ob不在li中会报错
#t.remove(0) #ValueError: list.remove(x): x not in list
t.remove(11)  #只删除了一个11， ['a', 22, 33, 11, 44, 55, 66, 77, [88, 99, 100], 111, 122, 133]
print(t)

#弹出元素
#li.pop(idx)会将索引idx处的元素删除，并返回这个元素
t1 = t.pop(1)
print("pop:",t1,";result:", t)  #pop: 22 ;result: ['a', 33, 11, 44, 55, 66, 77, [88, 99, 100], 111, 122, 133]

#排序
#li.sort()会将列表中的元素按照一定的规则进行排序
#t.sort()
#print(t) # 数字和字母同时存在时不能使用此函数，TypeError: unorderable types: int() < str()
t2 = [3,9,4,6,5,3] #[3, 3, 4, 5, 6, 9]
t2.sort()
print(t2)

#如果不想改变原来列表中的值，可以使用sorted函数：
t3 = [10, 1, 11, 13, 11, 2]
t4 = sorted(a)
print(t3)  #[10, 1, 11, 13, 11, 2]
print(t4)   #[33, 410, 511]

#列表反向
#li.reverse()  会将列表中的元素从后向前排列
t5 = [10, 1, 11, 13, 11, 2]
t5.reverse()
print(t5)  #[2, 11, 13, 11, 1, 10]
#如不想改变原来列表中的值，可以使用这样的方法
t6 = [10, 1, 11, 13, 11, 2]
t6_a = t6[::-1]
print(t6)
print(t6_a)
