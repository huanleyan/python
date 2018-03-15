#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function #兼容python3的print写法
from __future__ import unicode_literals #兼容python3的编码处理

'''
@description: 属性操作
@author:chenghuan
'''

class Clothes(object):
    def __init__(self, price):
        self.price = price
    #使用@property就变成属性了，默认是只读属性
    @property
    def discount_price(self):
        return self.price*0.8
    #这里discount_price就是一个只读不写的属性（注意是属性，不是方法）
    #price是可读写的属性
my_cloth = Clothes(100)
print(my_cloth.discount_price)   #80.0
#可以修改price属性来修改discount_price
my_cloth.price = 200
print(my_cloth.discount_price)   #160
#my_cloth.discount_price()会报错，因为discount_price是属性，不是方法
#my_cloth.discount_price = 100也会报错，因为是只读属性

#对于@property生成的只读属性，我们可以使用@attr.setter修饰符来使这个属性变成可写的
class ClothesTest(object):
    def __init__(self, price):
        self.price = price
    @property
    def discount_price(self):
        return self.price*0.8
    @discount_price.setter
    def discount_price(self, new_price):
        self.price = new_price*1.25
my_cloth = ClothesTest(100)
print(my_cloth.discount_price)  #80    100*0.8
my_cloth.price = 220
print(my_cloth.discount_price)   #176    220*0.8
#修改discount_price属性
my_cloth.discount_price = 270
print(my_cloth.price)   #337.5   270*1.25
print(my_cloth.discount_price)   #270     337.5*0.8



#一个等价的替代如下，用方法：
class ClothesTest(object):
    def __init__(self, price):
        self.price = price
    def get_discount_price(self):
        return self.price*0.8
    def set_discount_price(self, new_price):
        self.price = new_price * 1.25
    discount_price = property(get_discount_price, set_discount_price)
