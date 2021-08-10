# !/usr/bin/python3
# coding:utf-8
# author:panli
import os
import configparser


def base_dir(filename=None):
	return os.path.join(os.path.dirname(__file__), filename)


def get_Linux(linux='Linux'):
	List1 = []
	config = configparser.ConfigParser()
	config.read(base_dir('congif.ini'))
	ip = config.get(linux, 'ip')
	port = config.get(linux, 'port')
	username = config.get(linux, 'username')
	password = config.get(linux, 'password')
	# print(ip, port, username, password)
	List1.append(ip)
	List1.append(port)
	List1.append(username)
	List1.append(password)
	return List1


def f1(listname):
	for u in listname:
		print(u)


f1(get_Linux())
