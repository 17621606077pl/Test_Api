# !/usr/bin/python3
# coding:utf-8
# author:panli
"""
课堂笔记写法，通过类的实例化对象来实现登陆注册功能， 不用input输入用户信息
"""
import json
import sys


class Day8Login(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def getusername(self):
		return self.username

	def setusername(self, username):
		return self.username == username

	def getpassword(self):
		return self.password

	def setpassword(self, password):
		return self.password == password

	def login(self):
		with open('json.txt', 'r') as f:
			temp = f.read()
			str1 = temp.split('|')
		if self.username == str1[0] and self.password == str1[1]:

			return True

		else:

			return False

	def register(self):
		temp = self.username + '|' + self.password
		with open('json.txt', 'w') as f:
			f.write(temp)
		print('您好！{0},恭喜你已经注册成功'.format(self.username))

	def info(self):
		with open('json.txt', 'r') as f:
			temp = f.read()
			list1 = temp.split('|')
		if self.login():
			print('您好！{0},恭喜你已经登陆成功，欢迎进入系统'.format(list1[0]))
		else:
			print('Sorry, 很遗憾，登陆失败，请检查您的账号是否正确？')


if __name__ == "__main__":

	log = Day8Login('panli', '999')

	while True:
		rest = int(input('请选择：1、登陆 2、注册 3、退出 \n'))
		if rest == 1:
			log.info()

		elif rest == 2:
			log.register()

		elif rest == 3:
			sys.exit()
			exit(1)

		else:
			print('输入错误，请继续')
		continue
