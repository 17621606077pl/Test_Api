# !/usr/bin/python3
# coding:utf-8
# author:panli
import pytest
import json
from base.method import Requests
from utils.operationYaml import OperationYaml

req = Requests()
oper = OperationYaml()


# oper.readYaml()打印结果是一个列表形式的多个用例，然后datas就是参数化列表中的数据一条一条去执行，
# 利用 oper.readYaml()文件读取到的列表数据（用例），中的url,请求数据，去发送请求，然后把请求成功的结果信息与列表中的期望结果去对比是否一致
# 需要注意的是方法中的参数datas要和参数方法的datas一样
@pytest.mark.parametrize('datas', oper.readYaml())
def test_login(datas):
	r = req.post(
		url=datas['url'],
		json=datas['data'])

	assert datas['expect'] in json.dumps(r.json(), ensure_ascii=False)

	# ensure_ascii=False显示成中文
	# print(json.dumps(r.json(), ensure_ascii=False))


if __name__ == '__main__':
	pytest.main('-s', '-v', 'Test_login1.py')
