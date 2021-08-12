# !/usr/bin/python3
# coding:utf-8
# author:panli
# !/usr/bin/python3
# coding:utf-8
# author:panli

import xlrd
from comment.public import filePath
import json


class ExcelVarles:
	caseID = "测试用例ID"
	caseModel = "模块"
	caseName = "接口名称"
	caseUrl = "请求地址"
	casePre = "前置条件"
	method = "请求方法"
	paramsType = "请求参数类型"
	params = "请求参数"
	ecpect = "期望结果"
	isRun = "是否运行"
	hearders = "请求头"
	status_code = "状态码"


class OperationExcel:
	""" 该类是用于打开excel第一个sheet，及该页的总行，总列， 或单元格信息"""
	def getSheet(self):
		sheet = xlrd.open_workbook(filePath('comment/data', 'api.xls'))
		""" 返回excel中第一个sheet信息"""
		return sheet.sheet_by_index(0)

	@property
	def getExcelDatas(self):
		datas = []
		title = self.getSheet().row_values(0)

		for row in range(1, self.getSheet().nrows):
			Row_Values = self.getSheet().row_values(row)
			datas.append(dict(zip(title, Row_Values)))
		return datas

	def Runs(self):
		"""获取是否可执行的测试用例"""
		runs_list = []
		for item in self.getExcelDatas:
			runs = item[ExcelVarles.isRun]
			if runs == 'y':
				runs_list.append(item)
		return runs_list

	def params(self):
		"""对请求参数为空时做处理"""
		params_list = []
		for item in self.Runs():
			params = item[ExcelVarles.params]
			if len(str(params).strip()) == 0: pass
			elif len(str(params).strip()) >=0:
				params = json.loads(params)
				# print(params)
		return params

	def case_prev(self, casePrev):
		"""
		:param casePrev: 根据传入前置条件的value值casePrev，找到前置条件方法本身并去执行它拿到结果信息如token
		:return:
		"""
		# self.runs() 是获取所有可执行的测试用例
		for item in self.cese_list():
			if casePrev in dict(item).values():
				"""在所有可执行的测试用例的Values中找到第一个value值是login的，就直接返回，不再继续循环，
				也就说明第一个value是login的话也是登陆的请求，所以拿到它直接返回"""
				return item
		return None  # 都没有的话返回None

	def prevHeardes(self, prevResult_token):
		"""把动态token替换到被关联的测试用例中的请求头中的token变量"""
		for item in self.Runs():
			headers= item[ExcelVarles.hearders]
			if '{token}' in headers:
				hearder =str(headers).replace('{token}', prevResult_token)
				return json.loads(hearder)

	def cese_list(self):
		"""
		获取Excel中所有的测试用例，可执行的和不可执行的
		:param casePrev:
		:return:
		"""
		case = list()
		for item in self.getExcelDatas:
			case.append(item)
		return case  # 此处返回for循环中的所有用例


if __name__ == '__main__':
	oper = OperationExcel()
	# print(oper.prevHeardes('jjjssjsjjsjsj'))
	# print(oper.params())
	# print(oper.case_prev('login'))








