#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
字符串的的索引及切分操作
'''
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

s ='good morning'
print(s)
print(s[0])
print(s[-2])

#分片用来从序列中提取想要的子序列 step 表示取值间隔大小，如果没有默认为1。
#用法为var[start:end:step]

print(s[-3:]) #ing
print(s[:-3]) #goods morn
print(s[:]) #goods morning
print(s[::2]) #go morn
print(s[::-1]) #gninrom doog
print(s[:100]) # good morning
