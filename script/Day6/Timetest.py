# !/usr/bin/python3
# coding:utf-8
# author:panli

import time as t

# 获取时间戳
print(int(t.time()))
# 获取当前时间
print(t.strftime('%y-%m-%d %H:%M:%S', t.localtime()))
