# !/usr/bin/python3
# coding:utf-8
# author:panli

# 导入Flask类
from flask import jsonify
from flask import Flask
from flask import render_template
from flask import request

# 实例化，可视为固定格式
app = Flask(__name__)


# route()方法用于设定路由，类似spring
@app.route('/helloworld')
def hello():
	return 'hello, world'


# 配置路由，当请求get.html时提交get_html处理
@app.route('/get.html')
def get_html():
# 使用render_template()方法重定向到templates文件夹下查找get.html文件
	return render_template('/get.html')


# 配置路由，当请求post.html时候，交由post_html()处理
@app.route('/post.html')
def post_html():
# 使用render_template()方法重定向到templates文件夹下的post.html文件
	return render_template('/post.html')


# 配置路由，当请求deal_request时，交由deal_request()处理
# 默认处理get请求，我们通过method参数指明也处理post请求
# 当然还可以直接指定method=['post']只处理post请求，这样下面就不需要if了
@app.route('/deal_request', methods=['GET', 'POST'])
def deal_request():
	if request.method == 'GET':
		# get通过request.args.get('q', '')形式获取参数值
		get_q = request.args.get('q', '')
		return render_template('result.html', result=get_q)
	elif request.method == 'POST':
		# post通过request.form["param_name"]形式获取参数值
		post_q = request.form['q']
		return render_template('result.html', result=post_q)


@app.route('/rest_test', methods=['POST'])
def hello_world():
	"""
	通过request.json以字典格式获取post内容
	通过jsonify实现返回json格式
	:return:
	"""
	post_param = request.json
	result_dict = {
		'result_code': 200,
		'post_param': post_param
	}
	return jsonify(result_dict)


if __name__ == '__main__':
	"""app.run("host", "port", 'debug', "options")"""
	app.run()


