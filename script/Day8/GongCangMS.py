# !/usr/bin/python3
# coding:utf-8
# author:panli

"""
__call__内置方法，对象实例化的时候直接返回__call__的内容，使用该方法可以模拟静态方法
静态方法被调用的时候直接类名.方法名()
"""


class P1(object):
	def __new__(cls, *args, **kwargs):
		print('call方法')

pp = P1()

"""
__str__内置对象代表的含义,返回一个字符串，通过它可以把对象和字符串关联起来，
方便某些程序的实现，该字符串某个类
实现了__str__后，可以直接使用print()语句输出对象，也可以通过函数str来触发__str__的执行
"""
