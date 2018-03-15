#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

#模块
#python会将所有.py结尾的文件认定为python的代码文件
#__name__属性
#有时候我们想将一个.py文件即当做脚本，又能当做模块用，这个时候可以使用__name__属性

PI = 3.14

def get_sum(lst):
    total = 0
    for v in lst:
        total = total +v
    return total

def test():
    lt = [1,2,3]
    #python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常。
    assert(get_sum(lt)==6)
    print('test pass')

if __name__ == '__main__':
    test()

#上文保存为ex.py
#可以从模块中导入ex变量
from ex import PI,get_sum

print(PI)   #3.14
print(get_sum([2,3]))   #5

#删除文件
import os
os.remove('ex.py')

#__init__.py 表示foo是一个包，他可以是个空文件夹
