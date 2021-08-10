# !/usr/bin/python3
# coding:utf-8
# author:panli
import json
import os


def readJson():
	return json.load(open('login.json', 'r', encoding='utf-8'))['item']


print(readJson())
