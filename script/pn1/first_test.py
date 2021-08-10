# !/usr/bin/python3
# coding:utf-8
# author:panli

# 常规写法
def test():
    list1 = [1, 2, 3, 4, 5]
    # print(dir(list1))
    # 实现列表中每个数都加上100
    list2 = []
    for x in list1:
        x += 100
        list2.append(x)
    # print(list2)


test()


# map方法写法
def f(a):
    return a + 100


list1 = [1, 2, 3, 4, 5]
list3 = [7, 8, 9]
# map一句话搞定,注意使用map时要强制转换成list列表
print(list(map(f, list1)))
# 再换map结合lambda写法, 注lambda是命名匿名函数的意思
print(list(map(lambda x: x+100, list1)))
print(list(map(lambda a, b: a+b, list1, list3)))
print(list(map(lambda a, b: (a+b, a*b), list1, list3)))
# filter函数 是用来过滤表达式的
print(list(filter(lambda a: a % 2 == 0, list1)))
