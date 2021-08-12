# !/usr/bin/python3
# coding:utf-8
# author:panli
import xlrd
from comment.public import filePath
from utils.operationYaml import OperationYaml
from comment.public import *


class ExcelNColes:
	""" 封装excel中所有的列值，因为每列的信息值都是对应的"""
	caseId = 0
	desc = 1
	url = 2
	method = 3
	data = 4
	expect = 5

	@property
	def getCaseId(self):
		return self.caseId

	@property
	def getDesc(self):
		return self.desc

	@property
	def getUrl(self):
		return self.url

	@property
	def getMehtod(self):
		return self.method

	@property
	def getData(self):
		return self.data

	@property
	def getExpect(self):
		return self.expect


class OperationExcel(OperationYaml):
	""" 该类是用于打开excel第一个sheet，及该页的总行，总列， 或单元格信息"""
	def getSheet(self):
		sheet = xlrd.open_workbook(filePath('comment/data', 'books.xls'))
		""" 返回excel中第一个sheet信息"""
		return sheet.sheet_by_index(0)

	@property
	def getRows(self):
		""" 获取总行数,该方法返回getSheet方法中第一个sheet栏的所有总行数"""
		return self.getSheet().nrows

	@property
	def gerCols(self):
		""" 获取总列数"""
		return self.getSheet().ncols

	def getValue(self, row, col):
		""" 获取单元格中的值"""
		return self.getSheet().cell_value(row, col)

	def getCaseID(self, row):
		return self.getValue(row=row, col=ExcelNColes().getCaseId)

	def getUrl(self, row):
		url = self.getValue(row=row, col=ExcelNColes().getUrl)
		if '{bookID}' in url:
			return str(url).replace('{bookID}', ReadContent())
		else:
			return url

	def getDesc(self, row):
		return self.getValue(row=row, col=ExcelNColes().getDesc)

	def getMethod(self, row):
		return self.getValue(row=row, col=ExcelNColes().getMehtod)

	def getData(self, row):
		return self.getValue(row=row, col=ExcelNColes().getData)

	def getExcept(self, row):
		return self.getValue(row=row, col=ExcelNColes().getExpect)

	def getJson(self, row):
		return self.ReadDictYaml()[self.getValue(row=row, col=ExcelNColes().getData)]


if __name__ == '__main__':
	oper = OperationExcel()
	# print(oper.getValue(row=2, cols=ExcelNColes().CaseId()))
	# print(oper.getCaseID(row=1))
	# print(oper.getDesc(row=1))
	# print(oper.getUrl(row=1))
	# print(oper.getMethod(row=1))
	# print(oper.getExcept(row=1))
	# print(oper.getJson(row=2))
