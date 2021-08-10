# !/usr/bin/python3
# coding:utf-8
# author:panli
import pytest
import unittest
import HTMLTestRunner
import time
import os


def allTest():
	suite=unittest.TestLoader().discover(
		start_dir=os.path.dirname(__file__),
		pattern='test_*.py',
		top_level_dir=None)
	return suite


def getNowTime():

		return time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))


def run():
	fp = os.path.join(os.path.dirname(__file__), 'report', getNowTime()+'testReport.html')
	HTMLTestRunner.HTMLTestRunner(
		stream=open(fp, 'wb'),
		title='自动化测试报告',
		description='自动化测试报告详细信息').run(allTest())


if __name__ == '__main__':
	run()
