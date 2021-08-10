# !/usr/bin/python3
# coding:utf-8
# author:panli
import unittest
from selenium import webdriver
import time


class TestCase(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()

	def test_map(self):
		""" 验证首页百度地图链接是否可以正常跳转"""
		self.driver.find_element_by_partial_link_text('地图').click()
		# print(self.driver.current_url, '红红火火恍恍惚惚或或哈哈哈哈或')
		time.sleep(3)
		self.assertEqual(self.driver.current_url, 'https://www.baidu.com/')

	def test_news(self):
		""" 验证码首页百度新闻是否"""
		self.driver.find_element_by_partial_link_text('新闻').click()
		time.sleep(3)
		self.assertEqual(self.driver.current_url, 'https://www.baidu.com/')


if __name__ == '__main__':
	unittest.main(verbosity=2)
