# !/usr/bin/python3
# coding:utf-8
# author:panli

"""方法的继承
子类可以重写父类的方法
"""


class Fruit(object):

	def eat(self):
		print('水果好吃')


class Apple(Fruit):
	def __init__(self, color):
		self.color = color

	def eat(self):
		print('苹果变成{0}就说明熟了，可以吃了'.format(self.color))


app = Apple(u'红色')
app.eat()
