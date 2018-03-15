#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理


#与操作系统进行交互：os模块
import os

#文件路径操作
#删除指定路径的文件，路径可以是全名，也可以是当前工作目录下的路径
os.remove(path)或os.unlink(path)

#删除文件，并删除中间路径中的空文件夹
os.removedirs(path)

#将当前的工作目录改变为指定的路径，相当于shell下的cd命 令。
os.chdir(path)

#获取当前工作目录，即当前python脚本工作的目录路径
os.getcwd()

#返回当前目录：（’ . ‘）
os.curdir
#os.curdir表示当前目录更准确,listdir返回目录所有文件及文件夹的目录列表
list_all = os.listdir(os.curdir)

#重命名文件
os.rename(old, new)
#重命名文件，如果中间路径的文件夹不存在，则创建文件夹
os.renames(old, new)

#返回给定目录下的所有文件夹和文件名，不包括‘.’(当前目录)和‘..’（父及目录）以及子文件夹下的目录
os.listdir(path)

#产生新文件夹
os.mkdir(name)

#产生新文件夹，如果中间路径的文件夹不存在，则创建文件夹
os.mkdirs(name)

#系统常量
#当前操作系统的换行符
#window为\r\n  unix为\n
os.linesep
#当前操作系统的路径分隔符
os.sep
#当前操作系统的环境变量中的分隔符window为; unix为：
os.pathsep

#os.environ是一个存储所有环境变量的值的字段，可以修改
os.environ

#os.path模块
import os.path

#检测一个路径是否为普通文件
os.path.isfile(path)
#检测一个路径是否为文件夹
os.path.isdir(path)

#检测路径是否存在
os.path.exists(path)

#检测路径是否为绝对路径
os.path.isabs(path)

#拆分一个路径为(head, tail)两部分
os.path.split('c:/tem/b.txt')     #('c:/tem', 'b.txt')

#使用系统的路径分割符，将各个部分合成一个路径
a = 'c:/tem'
b = 'b.txt'
os.path.join(a,b)

'''
列出文件夹下所有的文件
dir_path  :父文件夹路径

os.walk 的返回值是一个生成器(generator),也就是说我们需要不断的遍历它，来获得所有的内容。
每次遍历的对象都是返回的是一个三元组(root,dirs,files)
root 所指的是当前正在遍历的这个文件夹的本身的地址
dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
如果topdown 参数为真，walk 会遍历top文件夹，与top文件夹中每一个子目录。

'''
def get_files(dir_path):
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            print("parent is:", parent)
            print("filename is:", filename)
            print("full name of the file is:", os.path.join(parent, filename))
dir = 'C:\Windows\System32\'
get_files(dir)




























#
