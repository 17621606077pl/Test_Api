# !/usr/bin/python3
# coding:utf-8
# author:panli

import requests


class Method():
	def get(self, url, **kwargs):
		try:
			return requests.get(url=url, **kwargs)

		except:
			raise print('请求出错')


obj = Method()
r = obj.get(url='http://www.baidu.com')
print(r.status_code)
print(r.text)
