#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 16:53
# @Author  : Yao
import sys
from os import path
d = path.dirname(__file__)
from githut_test2.demo.demo import *
test()

parent_path = path.dirname(d) #获得d所在的目录,即d的父级目录
print(parent_path)

sys.path.append(parent_path)

from githut_test2.demo import demo
demo.test()

'''
parent_path  = path.dirname(parent_path) ##获得parent_path所在的目录即parent_path的父级目录
print(parent_path)
'''