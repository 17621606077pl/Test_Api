# !/usr/bin/python3
# coding:utf-8


# author:panli
''' 类 由一系列的属性和方法组成'''


'''
# 对象的创建：就是类实例化的过程
三个特性
1、对象的句柄，区分不同的对象
2.属性
3.方法
'''


class Person(object):
	#类属性
	gongtong = 'china'

	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs

	def info(self):
		print(self.args, self.kwargs.values())


# 如果动态参数有元组和字典，形式参数要写在默认参数前面
per = Person('xian', name='wuya', age=18)
per.info()

per2 = Person('sh', name='pl', age=20, marry='未婚')
per2.info()

# 类属性属性对象也属于类
per3 = Person('测试', 20)
print(per3.gongtong)  # 属于对象
print(Person.gongtong)  # 属于类


