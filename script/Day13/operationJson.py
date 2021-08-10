#!/usr/bin/env python
#!coding:utf-8


import  json


def readJson():
	return json.load(open('login.json','r'))['item']
