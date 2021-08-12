# !/usr/bin/python3
# coding:utf-8
# author:panli
from flask import Flask, jsonify
from flask_restful import Api, reqparse, Resource
import json

app = Flask(__name__)
api = Api(app)


class Test_ApiView(Resource):
	def get(self):
		return {'status':0, 'msg': 'ok', 'data': ''}

	def post(self):
		parse = reqparse.RequestParser()
		parse.add_argument('username', type=str, required=True, help='username参数不能为空')
		parse.add_argument('password', type=str, required=True, help='密码不能为空')
		parse.add_argument('age', type=int, required=True, help='年龄必须为正整数')
		parse.add_argument('sex', type=str, help='性别只能是男或女', choices=['男', '女'])
		return jsonify(parse.parse_args())


api.add_resource(Test_ApiView, '/login/', endpoint='login')


if __name__ == '__main__':
	app.run(debug=True)



