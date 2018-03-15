#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

#读文件
#使用open函数或者file函数来读文件，使用文件名的字符串作为输入参数
f = open('chenghuan.txt')
f = file('chenghuan.txt')

#默认以读的方式打开文件，如果文件不存在会报错
#可以使用read方法来读取文件中的所有内容
text = f.read()
print(text)

#按照行读入内容，readlines方法返回一个列表，每个元素代表文件中每一行的内容
f = open('chenghuan.txt')
text = f.readlines()
print(text)
f.close()

#事实上我们可以将f放在一个循环中，得到它每一行的内容
f = open('chenghuan.txt')
for line in f:
    print(line)
f.close()


#写文件
#我们使用open函数的写入模式来写文件
f = open('chenghuan.txt', 'w')
f.write('hello chenghuan')
f.close()


#二进制文件
#二进制读写模式wb
import os
f = open('binary.bin', 'wb')
w.write(os.urandom(10))
f.close()

f = open('binary.bin', 'rb')
print(repr(f.read()))
f.close()

#with方法
#事实python提供了更安全的方法，当with块的内容结束后，python会自动调用它的close方法，确保读写的安全
with open('chenghuan.txt', 'w') as f:
    for i in range(100):
        x = 1.0/(i-1000)
        f.write('hello world'+str(i)+'\n')
