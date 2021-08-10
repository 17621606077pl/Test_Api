# !/usr/bin/python3
# coding:utf-8
# author:panli

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

ls = list(num for num in list1 if num % 2 == 0)
print(ls)
