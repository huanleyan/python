#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

'''
@description: 共有，私有和特殊方法和属性
@author:chenghuan
'''
#special方法和属性，即以__开头和结尾的属性和方法
#私有方法和属性，以_开头，不过不是真正私有，而是可以调用的
#以__开头但是不以__结尾的属性是更加特殊的方法，调用方式也不同
class MyDemoClass(object):
    def __init__(self):
        print("special.")
    def _get_name(self):
        print("_get_name is private method")

    def get_value(self):
        print("get_value is public method")

    def __get_type(self):
        print("__get_type is really special method.")

demo = MyDemoClass()
demo.get_value()
demo._get_name
