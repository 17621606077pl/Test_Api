# !/usr/bin/python3
# coding:utf-8
# author:panli
# !/usr/bin/python3
# coding:utf-8
# author:panli
import requests
import json
import csv
import unittest
import ddt

def getHearder():
	header = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55',
		          'referer': 'https://www.lagou.com/wn/jobs?cl=false&fromSearch=true&kd=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&city=%E4%B8%8A%E6%B5%B7&pn=1',
		          'cookie': 'user_trace_token=20210722175302-3494da11-d18a-46de-8341-8aced6d47045; _ga=GA1.2.2096563177.1626947584; LGUID=20210722175303-d9107b08-2bcb-4bb5-bc4f-35e54a788640; gate_login_token=cceaace95ccbd4d0e121a9f7f342822144583ebaccb2bd98; LG_LOGIN_USER_ID=1eee7fee0ecaa4b6c3f14b654026b2a120daaea567453a1a; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=98; privacyPolicyPopup=false; index_location_city=%E4%B8%8A%E6%B5%B7; RECOMMEND_TIP=true; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1626947584,1626947589,1627351788; __SAFETY_CLOSE_TIME__8556999=1; _gid=GA1.2.1304316056.1627351801; WEBTJ-ID=20210727141940-17ae69e6d1c43-0472d410165dc-7e687a6e-1338645-17ae69e6d1d56d; sensorsdata2015session=%7B%7D; JSESSIONID=ABAAAECABFAACEAC1E637D9584A688359ED1F43AAE160CE; _putrc=402C16F72BC8F765; login=true; unick=%E6%BD%98%E4%B8%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%228556999%22%2C%22%24device_id%22%3A%2217acda222f595f-07362a4c19c9fc-7a697f6c-1338645-17acda222f7bd5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2292.0.4515.107%22%7D%2C%22first_id%22%3A%2217acda222f595f-07362a4c19c9fc-7a697f6c-1338645-17acda222f7bd5%22%7D'

	}

	return header


url = 'https://www.lagou.com/jobs/v2/positionAjax.json'


@ddt.ddt
class Test_LaGou(unittest.TestCase):
	@ddt.data((1,), (2,), (3,), (4,))
	@ddt.unpack
	def test_lagou(self, page):
		r = requests.post(
			url=url,
			headers=getHearder(),
			data={'first': True, 'city': '上海', 'page': page, 'kd': '自动化测试工程师'})
		self.assertEqual(r.json()['success'],True)
		# print(r.json()['content']['positionResult']['result'][0]['city'], '哈哈哈哈哈哈哈')


if __name__ == '__main__':
	unittest.main(verbosity=2)







