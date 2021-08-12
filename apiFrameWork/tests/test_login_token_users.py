# !/usr/bin/python3
# coding:utf-8
# author:panli
from base.method import Requests
from utils.operationExcelDemo import ExcelVarles, OperationExcel
import json
import pytest
from comment.public import *
import allure

oper = OperationExcel()
obj = Requests()


@pytest.mark.parametrize('datas', oper.Runs())
def test_login_token_user(datas):
	""" 对请求参数做反序列化处理"""
	params = datas[ExcelVarles.params]
	if len(str(params).strip()) == 0:pass
	elif len(str(params).strip()) >=0:
		# print(json.loads(params))
		params = json.loads(params)
	# oper.params()

	""" 对请求头做参数化处理，，注意去空格 去的是双引号两头的空格，并不去字符串之间的空格"""
	header= datas[ExcelVarles.hearders]
	if len(str(header).strip()) == 0:pass
	elif len(str(header).strip()) >=0:
		header = json.loads(header)

	"""
	1、先获取到所有带前置条件的测试用例的同一个前置测试用例的测试
	2、找到之后先执行前置条件测试点
	3、获取到的结果信息
	4、拿它的结果信息替换对应的测试点的变量
	"""

	# 执行前置测试点，拿到token结果信息
	r = obj.post(
		# datas[ExcelVarles.casePre获取到前置条件本身的测试方法值如前置条件是先login登陆
		url=oper.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.caseUrl],
		json=json.loads(oper.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.params]))
	prevResult_token = r.json()['access_token']
	# 替换被关联的测试用例中的请求头信息中的token变量
	header =oper.prevHeardes(prevResult_token)

	status_code = int(datas[ExcelVarles.status_code])

	def case_assert_Result(r):
		"""断言方法，判断Excel表中读取的期望结果栏信息在不在请求成功后的响应信息中"""
		assert r.status_code == status_code or 201
		assert datas[ExcelVarles.ecpect] in json.dumps(r.json(), ensure_ascii=False)

	def setUrl():
		"""ReadContent()读取添加用户成功后写入的id,然后替换url中的{bookID}"""
		url = str(datas[ExcelVarles.caseUrl]).replace('{bookID}', ReadContent())
		return url

	if datas[ExcelVarles.method] == 'get':
		if '/books' in datas[ExcelVarles.caseUrl]:
			r = obj.get(
				url=datas[ExcelVarles.caseUrl],
				headers=header)
			case_assert_Result(r=r)
		else:
			r = obj.get(
				url=setUrl(),
				headers=header)
			case_assert_Result(r=r)

	elif datas[ExcelVarles.method] == 'post':
		r = obj.post(
			url=datas[ExcelVarles.caseUrl],
			json=params,
			headers=header)
		# 把添加用户成功的id写入到文件中，注入写入到文件中不能是int型，一定得是字符串
		WriteContent(content=str(r.json()[0]['datas']['id']))
		case_assert_Result(r=r)

	elif datas[ExcelVarles.method] == 'delete':
		r = obj.delete(
			url=setUrl(), headers=header)
		case_assert_Result(r=r)

	elif datas[ExcelVarles.method] == 'put':
		r = obj.put(
			url=setUrl(),
			json=params,
			headers=header)
		case_assert_Result(r=r)


if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_login_token_users.py", "--alluredir", "./report/result"])
	import subprocess
	subprocess.call('allure generate ./report/result/ -o report/html --clean',shell=True)
	subprocess.call('allure open -h 127.0.0.1 -p  8088 ./report/html',shell=True)

