# !/usr/bin/python3
# coding:utf-8
# author:panli

'''
函数的几个用法：
1、函数可以当做一个变量使用
2、函数的参数可以是函数
3、函数是可以嵌套的
'''


def f1():
	print('hello')


# per = f1()
# per    # 函数当做变量使用，下面把函数赋值给一个变量再调用


def f2(a):
	return a


# f2(f1())  # 函数的参数可以是函数


def login(username='admin', password='123'):
	if username == 'admin' and password == '123':
		return 'token:qazxsw1233'
	else:
		return '用户名或密码错误'


def profile(token):
	if token == 'token:qazxsw1233':
		return '欢迎访问admin个人主页'

	else:
		return '请登陆到系统'


	# 代表的是 函数的参数可以是函数
# print(profile(login()))  # 因为login上面是默认参数，所以这里可以不传参，，但是上面如果是形式参数这里必传


# 函数是可以嵌套的
def f3():
	def f4():
		return 'hello, world'
	return f4()


# print(f3())


def getInfo(fn):
	print('python自动化课程')
	fn()


@getInfo
def f5():
	print('网易云')


@getInfo
def f6():
	print('51CTO课堂')

