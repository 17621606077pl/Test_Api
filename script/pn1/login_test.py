# !/usr/bin/python3
# coding:utf-8
# author:panli

def inOut():
	username = input('请输入用户名：\n')
	password = input('请输入密码：\n')
	return username, password


def register():
	username, password = inOut()
	temp = username+'|'+password
	with open('json.txt', 'w') as f:
		f.write(temp)


def login():
	''' 登陆的函数 '''
	username, password = inOut()
	with open('json.txt', 'r') as f:
		info = f.read()
		# print(info)
		info = info.split('|')

	if username == info[0] and password == info[1]:
		return True
	else:
		False


# print(login())

def getNick(func):
	with open('json.txt', 'r') as f:
		info = f.read()
	info = info.split('|')
	if func:
		print('你好,{0}，欢迎登陆无涯课堂'.format(info[0]))
	else:
		print('请登陆系统')


if __name__ == "__main__":

	while True:
		t = int(input('1、注册 2、登陆 3、退出系统\n'))
		if t == 1:
			register()

		elif t == 2:
			getNick(login())

		elif t == 3:
			import sys
			sys.exit()

		else:
			print('输入错误，请继续')
			continue

