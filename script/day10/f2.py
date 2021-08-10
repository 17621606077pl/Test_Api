# !/usr/bin/python3
# coding:utf-8
# author:panli

import unittest
from selenium import webdriver
import time as t


class F2(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get("https://www.baidu.com/")
		t.sleep(5)


	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def test_baidu_001(self):
		""" 百度首页新闻连接的测试 """
		self.driver.find_element_by_link_text('新闻').click()
		t.sleep(3)

	def test_baidu_002(self):
		""" 首页测试验证地图的链接"""
		self.driver.find_element_by_partial_link_text('地图').click()
		t.sleep(2)


if __name__ == '__main__':
	unittest.main()
