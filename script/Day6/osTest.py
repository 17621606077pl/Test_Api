# !/usr/bin/python3
# coding:utf-8
# author:panli

import os

# os库最常用的是对目录的处理
# print(os)
# 当前文件的目录
# print(dir(os))

# 创建一个文件夹
# os.mkdir('d:/
# 对文件或目录重新命名
# os.rename('d:/log', 'd:/newlog')
# 对目录的处理
print(u'osTest.py当前文件的目录:', os.path.dirname(__file__))
print(u'获取当前文件的上级目录:', os.path.dirname(os.path.dirname(__file__)))
# print(u'获取当前文件的上级的上级目录:', os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# 实现Day3下login文件内容的读取
base_dir = os.path.dirname(os.path.dirname(__file__))
f = open(os.path.join(base_dir, 'Day3/login'), 'r')
print(f.read())


'''请求参数是不确定的，可能一个可能n个'''


def f(*args, **kwargs):
	return kwargs


print(f(name='wuya', age='18'))
print(f(name='wuya', age='18', address='xian'))
