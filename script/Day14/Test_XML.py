# !/usr/bin/python3
# coding:utf-8
# author:panli
import xml.dom.minidom
def getXML(value=None):
	xmlFile = xml.dom.minidom.parse("data.xml")
	db = xmlFile.documentElement
	itemList= db.getElementsByTagName(value)
	item = itemList[0]
	return item.firstChild.data


def getUser(parent='wuya', Child=None):
	xmlFile = xml.dom.minidom.parse("data.xml")
	db = xmlFile.documentElement
	itemList= db.getElementsByTagName(parent)
	item = itemList[0]
	return item.getAttribute(Child)


print(getUser(Child='address'))
