# !/usr/bin/python3
# coding:utf-8
# author:panli
import pytest
import requests
from 创建书籍.parameter.operationjson import readJson


@pytest.mark.parametrize('data', readJson())
def test_json_login(data):
	r = requests.get(
		url=data['request']['url'],
		json=data['request']['body']
	)
	print(data['response'][0])
	# print(r.json())
	# assert r.json() == data['response'][0]


if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_json_login.py"])
