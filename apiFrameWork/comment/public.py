# !/usr/bin/python3
# coding:utf-8
# author:panli
import os


# base_url = os.path.dirname(os.path.dirname(__file__))
# print(os.path.join(base_url, 'data', 'login.yaml')


def filePath(fileDir='data', fileName='login.yaml'):
	"""

	:param fileDir: 文件目录名
	:param fileName: 文件目录名下的文件名称
	:return:
	"""
	return os.path.join(
		os.path.dirname(os.path.dirname(__file__)), fileDir,  fileName)


def WriteContent(content):
	""" content参数代表是要写入的数据，如想要把id写入文件，那么只需要把id当参数传入就行
		filePath指定写入的文件目录路径及文件名称是在哪里  ，
		因为filePath方法本身有默认路径是fileDir='data', fileName='login.yaml
		如果默认也是在data文件下可以不传fileDir参数
		w 是只写模式'
		BookID是文件名，如果该目录下没有这个文件会自动创建一个"""
	with open(filePath(fileDir='comment/data', fileName='BookID'), 'w') as f:
		# 把要写入的内容强制转换成字符串再写入
		f.write(str(content))


def ReadContent():
	with open(filePath(fileDir='comment/data', fileName='BookID'), 'r') as f:

		return f.read()

