# !/usr/bin/python3
# coding:utf-8
# author:panli
"""
通过input让用户输入用户名密码来实现登陆注册功能
"""
import json
import sys


class ZC(object):
	def __init__(self, username=None, password=None):
		self.username = username
		self.password = password

	def InOut(self):
		self.username = input('请输入用户名：\n')
		self.password = input('请输入密码：\n')

	def login(self, *args, **kwargs):
		with open('json.txt', 'r') as f:
			temp = f.read()
			str1 = temp.split('|')
		if self.username == str1[0] and self.password == str1[1]:
			print('hhh', self.username, self.password, type(self.password))
			return True

		else:

			return False

	def register(self, *args, **kwargs):
		temp = self.username + '|' + self.password
		with open('json.txt', 'w') as f:
			f.write(temp)

	def info(self, *args):
		if self.login():
			print('恭喜进入到系统')
		else:
			print('Sorry, 很遗憾，登陆失败，请检查您的账号是否正确？')


if __name__ == "__main__":

	while True:
		rest = int(input('请选择：1、登陆 2、注册 3、退出 \n'))
		zz = ZC()
		if rest == 1:
			zz.info(zz.InOut())

		elif rest == 2:
			zz.register(zz.InOut())

		elif rest == 3:
			sys.exit()
			exit(1)

		else:
			print('输入错误，请继续')
		continue











