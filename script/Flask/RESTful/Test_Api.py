# !/usr/bin/python3
# coding:utf-8
# author:panli
"""
可以使用Flask-RESTful实现
路由设置为：
api.add_resource(UserListAPI, '/api/v1.0/users', endpoint='users')
api.add_resource(UserAPI, '/api/v1.0/users/<int:id>', endpoint='user')
"""
from flask import Flask, jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, reqparse, Resource

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

users = [
	{
		'id': 1,
		'username': '明明',
		'sex': 1
	},
	{
		'id': 2,
		'username': '王俊凯',
		'sex': 0

	}
]
# 验证字段的合法性
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='此字段格式有问题', location='json')
parser.add_argument('password', type=int, required=True, help='密码不能为空,且是整型', location='json')
parser.add_argument('age', type=int, required=True, help='年龄必填项', location='json')
parser.add_argument('sex', type=str, required=True, help='性别只能写男或女', choices=['男', '女'], location='json')


# 访问前需要提供用户名和密码
@auth.get_password
def get_password(username):
	if username == 'admin':
		return '123456'
	return None


class UserListAPI(Resource):
	decorators = [auth.login_required()]

	def get(self):
		return {'users': users}

	def post(self):
		args = parser.parse_args()
		user = {
			'id': users[-1]['id']+1,
			'username': args['username'],
			'sex': args['sex']
		}
		users.append(user)
		return {'user': user}, 201


class UserAPI(Resource):
	decorators = [auth.login_required()]

	def get(self, id):
		user = list(u for u in users if u['id'] == id)
		if len(user) == 0:
			abort(404)
		user = user[0]
		return {'user': user}

	def put(self, id):
		user = list(u for u in users if u['id'] == id)
		if len(user) == 0:
			abort(404)
		user = user[0]
		args = parser.parse_args()
		for k, v in args.items():
			if v != None:
				user[k] = v
			return {'user': user}

	def delete(self, id):
		user = list(u for u in users if u['id'] == id)
		if len(user) == 0:
			abort(404)
		users.remove(user[0])
		return jsonify({'result': '删除用户成功'})


api.add_resource(UserListAPI, '/api/v1.0/users', endpoint='users')
api.add_resource(UserAPI, '/api/v1.0/users/<int:id>', endpoint='user')


if __name__ == '__main__':
	app.run(debug=True)
