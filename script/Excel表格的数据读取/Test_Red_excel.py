# !/usr/bin/python3
# coding:utf-8
# author:panli

import xlutils
import xlrd
import os
from xlutils.copy import copy


def base_dir(filename=None):
	return os.path.join(os.path.dirname(__file__), filename)


work = xlrd.open_workbook(base_dir('api.xls'))
sheet = work.sheet_by_index(0)
print(sheet.nrows)
print(sheet.cell_value(4, 2))
old_content = copy(work)
ws = old_content.get_sheet(0)
ws.write(3, 2, '哈哈哈哈')
old_content.save(base_dir('excel.xls'))


