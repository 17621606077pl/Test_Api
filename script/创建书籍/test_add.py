# !/usr/bin/python3
# coding:utf-8
# author:panli
import pytest


@pytest.mark.parametrize('a, b, except', [
	[1, 1, 2],
	[1, 1, 2],
	[1, 1, 2],
	[1, 1, 2]
])
def add(a, b):
	return a + b


def test_add(a, b, expect):
	assert add(a, b) == expect


if __name__ == '__main__':
	pytest.main('test_add.py')
