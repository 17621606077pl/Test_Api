#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


import json
import requests

'''
序列化：把pyhton的数据类型转为str的类型过程
反序列化：str的类型转为python的数据结构
'''

# r=requests.post(url='https://ecapi.parkingwang.com/v5/login',
#                 headers={'Parkingwang-Client-Source':'ParkingWangAPIClientWeb',
#                          'Content-Type':'application/json;charset=UTF-8'},
#                 data=json.dumps({"username":"","password":""}))
# print str(r.text)
# print type(str(r.text))
#反序列化的知识，把str-->dict
# print json.loads(str(r.text))['msg']

'''文件的序列化与反序列化'''
r=requests.get(url='http://www.weather.com.cn/data/sk/101190408.html')
# print r.content.decode('utf-8')
#对文件进行序列化-->就是把服务端的响应数据写到文件中
json.dump(r.content,open('weather.json','w'))

#对文件的反序列化:就是读取文件的内容
'''
1.文件反序列化后，，类型是unicode
2.进行编码，把unicode类型转为str类型
3.然后使用反序列化的，把str转为字典类型
'''
dict1=json.loads((json.load(open('weather.json','r'))).encode('utf-8'))
print(dict1['weatherinfo']['city'])

'''
作业：
1.获取太苍的最低气温
'''


'''字典的序列化与反序列化'''
# dict1={'name':'wuya','age':18}
#
# #序列化:dict--->str
# dict_str=json.dumps(dict1)
# print u'序列化后的结果信息:'
# print dict_str,type(dict_str)
#
# #反序列化
# str_dict=json.loads(dict_str)
# print u'反序列化后的结果信息:'
# print str_dict,type(str_dict)

'''列表的序列化与反序列化的过程'''
# list1=['admin','wuya','weike']
# #序列化:
# list_str=json.dumps(list1)
# print u'序列化后的结果信息：'
# print  list_str,type(list_str)
# #反序列化的过程
# str_list=json.loads(list_str)
# print u'反序列化后的结果信息：'
# print  str_list,type(str_list)

'''元组的序列化与反序列化的过程'''
# tuple1=(1,2,3)
# #序列化
# tuple_str=json.dumps(tuple1)
# print u'序列化后的结果信息：'
# print  tuple_str,type(tuple_str)
#
# #反序列化
# str_tuple=json.loads(tuple_str)
# print u'反序列化后的结果信息：'
# print  str_tuple,type(str_tuple)





