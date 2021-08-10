# !/usr/bin/python3
# coding:utf-8
# author:panli
"""
使用Flask实现一个RESTful API服务的例子
路由设置，就是访问地址设置在每个函数上
"""
from flask import Flask, jsonify, make_response, request, abort
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = [
	{
		'id': 1,
		'username': '小明',
		'sex': 1
	},
	{
		'id': 2,
		'username': '小红',
		'sex': 0
	}
]


# 访问前需要提供用户名和密码
@auth.get_password
def get_password(username):
	if username == 'admin':
		return '123456'
	return None


# 友好的错误提示：没有权限
@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': '未授权'}), 403)


# 友好的错误提示：找不到资源页面
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': '找不到资源'}), 404)


# 返回所有用户信息
@app.route('/api/v1.0/users', methods=['GET'])
@auth.login_required
def get_users():
	return jsonify({'users': users})


# 返回一个用户的信息记录
@app.route('/api/v1.0/users/<int:user_id>', methods=['GET'])
@auth.login_required
def get_user(user_id):
	user = list(u for u in users if u['id'] == user_id)
	if len(user) == 0:
		abort(404)
	return jsonify({'user': user[0]})


# 插入一条用户记录
@app.route('/api/v1.0/users', methods=['POST'])
@auth.login_required()
def create_user():
	if not request.json or not 'username' in request.json or not 'sex' in request.json:
		print('你添加的没有username, sex字段：', request.json)
		abort(400)

	user = {
		'id': users[-1]['id']+1,
		'username': request.json['username'],
		'sex': request.json['sex']
	}
	users.append(user)
	return jsonify({'user': user}), 201


# 更新一个用户的记录
@app.route('/api/v1.0/users/<int:user_id>', methods=['PUT'])
@auth.login_required()
def update_user(user_id):
	user = list(u for u in users if u['id'] == user_id)
	if len(user) == 0:
		abort(400)
	user[0]['username'] = request.json.get('username', user[0]['username'])
	user[0]['sex'] = request.json.get('sex', user[0]['sex'])
	return jsonify({'user': user[0]})


# 删除一个用户
@app.route('/api/v1.0/users/<int:user_id>', methods=['DELETE'])
@auth.login_required()
def delete_user(user_id):
	user = list(u for u in users if u['id'] == user_id)
	if len(user) == 0:
		abort(404)
	users.remove(user[0])
	return jsonify({'result': True}), 204


if __name__ == '__main__':
	app.run(debug=True)
