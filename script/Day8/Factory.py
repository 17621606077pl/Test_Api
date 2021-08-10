# !/usr/bin/python3
# coding:utf-8
# author:panli

class Person(object):
	def __init__(self, name=None, gender=None):
		self.name = name
		self.gender = gender


class Male(Person):
	def __init__(self, name):
		print('Male' + name)

	def A(self):
		print('你好Male')


class Female(Person):
	def __init__(self, name):
		print('Female' + name)


class Factory(object):
	def getPerson(self, name, gender):
		if gender == 'M':
			return Male(name)
		elif gender == 'F':
			return Female(name)


if __name__ == '__main__':
	factory = Factory()
	factory.getPerson('Male', 'M')
