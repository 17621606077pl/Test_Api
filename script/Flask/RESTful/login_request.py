# !/usr/bin/python3
# coding:utf-8
# author:panli
"""
前面都是用postman进行接口测试的
使用Python的第三方库requests测试接口
"""
import requests,json

url = 'http://127.0.0.1:5000/api/v1.0'
auth = ('admin', '123456')

# 查询所有用户信息
r = requests.get(url + '/users', auth=auth)
# print(r.status_code, r.text)

# 在控制台输出时中文会用到unicode显示，可用下面方法显示中文
# print(json.dumps(json.loads(r.text), ensure_ascii=False))

# 查询单个用户信息
r = requests.get(url + '/users/1', auth=auth)
# print(r.status_code, r.text) 这样写显示的username会中文乱码
# print(json.dumps(json.loads(r.text), ensure_ascii=False))

# 添加用户信息
data = {
	'id': 1,
	'username': '小强强',
	'sex': 0
}

r = requests.post(url + '/users', auth=auth, json=data)
# print(json.dumps(json.loads(r.text), ensure_ascii=False))


# 修改
data = {
	'id': 3,
	'sex': 1,
	'username': '盼盼'
}
r = requests.put(url + '/users/3', auth=auth, json=data)
# print(json.dumps(json.loads(r.text), ensure_ascii=False))


# 删除
r = requests.delete(url + '/users/3', auth=auth)
print(r.status_code, r.text)
