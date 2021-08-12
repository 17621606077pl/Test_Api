# !/usr/bin/python3
# coding:utf-8
# author:panli

import pytest


def add(a, b):
	return a+b


@pytest.mark.parametrize('a, b, result', [
	(1, 2, 3),
	(2, 4, 6),
	(3, 4, 7)
])
# 注意 a, b参数要和参数化的参数保持一致
def test_add(a, b, result):
	assert add(a, b) == result


if __name__ == '__main__':
	pytest.main('-v', 'test_login')

