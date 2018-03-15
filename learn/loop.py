#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

#while 循环
i = 0
total = 0
while i<=100:
    total += 1
    i += 1
print(total)


#空容器会当成False，因此可以用while循环读取容器的所有元素
plays = set(['Hamlet', 'Mac', 'King'])
while plays:
    play = plays.pop()
    print('Perform', play)

#for循环
total = 0
for i in range(10000):
    total += i
print(total)
'''
Perform Ma
Perform Ha
Perform Ki
49995000
'''
#使用range写法有一个缺点，在循环之前会生成一个长度为10000的临时列表
#生成列表的问题在于，会有一定时间和内存消耗，长度越大消耗越明显
#使用xrange可以代替range函数，使用的时候并不会一次性生成所有的数据
total = 0
for i in xrange(10000):
    total += i
print(total)   # # 4999950000

## continue 语句
#遇到continue的时候，程序会跳出本次循环
values = [7,6,4,5,6,9,2]
for i in values:
    if i%2 != 0:
        #忽略奇数
        continue
    print(i)

#break语句
#遇到break的时候，程序会跳出循环，不管循环条件是不是满足
command_list = ['start','1','7', 'stop','11','aa']
while command_list:
    command = command_list.pop(0)
    if command == 'stop':
        break;
    print(command)

















#
