# !/usr/bin/python3
# coding:utf-8
# author:panli

import unittest
from selenium import webdriver


class BaiduLink(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.get('http://www.baidu.com')

	def tearDown(self):
		self.driver.quit()

	def test_baidu_so_enable(self):
		""" 首页：测试百度输入框是否可编辑"""
		so = self.driver.find_element_by_id('kw')
		self.assertTrue(so.is_enabled())

	def test_baidu_so(self):
		"""首页：测试百度的搜索功能"""
		so = self.driver.find_element_by_id('kw')
		so.send_keys('webdriver')
		self.driver.find_element_by_id('su').click()
		self.assertEqual(so.get_attribute('value'), 'webdriver')


if __name__ == '__main__':
	unittest.main(verbosity=2)
