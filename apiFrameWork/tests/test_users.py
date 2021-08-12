# !/usr/bin/python3
# coding:utf-8
# author:panli
from base.method import Requests
import pytest
from utils.operationExcel import OperationExcel
import json
from comment.public import *


class TestUsers:
	obj = Requests()
	operExcel = OperationExcel()

	def Result(self, r, row):
		assert r.status_code == 200 or 201
		""" json.dumps(r.json()响应数据是字典，因为从excel表格中读取出来的数据都是字符串格式的，所以需要对响应数据序列化成字符串后才能断言比较, 
		ensure_ascii=False 代表把内容中英文都支持显示"""
		assert self.operExcel.getExcept(row=row) in json.dumps(r.json(), ensure_ascii=False)

	def test_Users_001(self):
		""" 查询所有用户信息"""
		r = self.obj.get(url=self.operExcel.getUrl(row=1))
		self.Result(r=r, row=1)

	def test_Users_002(self):
		""" 添加用户"""
		r = self.obj.post(
			url=self.operExcel.getUrl(row=2),
			json=self.operExcel.getJson(row=2))
		# print(r.text)
		# print(r.json()['user']['id'])
		WriteContent(r.json()['user']['id'])
		# 断言请求是否成功，和期望结果是否在响应数据中
		self.Result(r=r, row=2)

	def test_Users_003(self):
		""" 查询单个用户信息"""
		r = self.obj.get(url=self.operExcel.getUrl(row=3))
		self.Result(r=r, row=3)

	def test_Users_004(self):
		""" 编辑用户信息"""
		r = self.obj.put(
			url=self.operExcel.getUrl(row=4),
			json=self.operExcel.getJson(row=4))
		# print(r.json())
		self.Result(r=r, row=4)

	def test_Users_005(self):
		""" 删除用户信息"""
		r = self.obj.delete(
			url=self.operExcel.getUrl(row=5))
		# print(r.text)
		# print(r.status_code)
		self.Result(r=r, row=5)


if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_users.py::TestUsers"])
