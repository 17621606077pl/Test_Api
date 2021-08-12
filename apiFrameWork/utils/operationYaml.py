# !/usr/bin/python3
# coding:utf-8
# author:panli
import yaml
from comment.public import filePath


class OperationYaml:
	def readYaml(self):
		with open(filePath('comment\data', 'login.yaml'), 'r', encoding='utf-8') as f:
			return list(yaml.safe_load_all(f))

	def ReadDictYaml(self, fileDir='comment/config', fileName='book.yaml'):
		with open(filePath(fileDir=fileDir, fileName=fileName), encoding='utf-8') as f:
			""" 以字典的形式读取yaml文件中的内容"""
			return yaml.safe_load(f)


if __name__ == '__main__':
	obj = OperationYaml()
	# print(obj.ReadDictYaml()['book_002'])
# obj.readYaml()
# print(obj.readYaml())
