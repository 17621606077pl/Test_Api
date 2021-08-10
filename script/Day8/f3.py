#!/usr/bin/env python 
# -*-coding:utf-8-*-
# author:wuya
"""
类:类是由一系列属性和方法组成
"""


class F1(object):
	pass


'''
对象的创建--->就是类实例化的过程
三个特性：
1.对象的句柄-->区分不同的对象
f2=F1()
f1=F1()
print(id(f1))
print(id(f2))
2.属性:
	共有属性
			类属性(共有的属性分离出来):它属于类，也属于对象,建议使用类调用
			实例属性:它只属于对象
			局部变量
	私有属性
3.方法
'''

'''类属性和实例属性的案例代码'''
# class Person(object):
# 	#类属性
# 	gongTong='china'
# 	def __init__(self,name,age):
# 		#实例属性
# 		self.name=name
# 		self.age=age
#
# 	def getName(self):
# 		return self.name
#
# 	def getAge(self):
# 		return self.age
#
# 	def setName(self,name):
# 		self.name=name
#
# 	def setAge(self,age):
# 		self.age=age
#
# 	def info(self):
# 		return u'name:{0},age:{1},来自:{2}'.format(self.getName(),self.age,self.gongTong)

# per=Person('wuya',18)
# print(per.gongTong)
# print(Person.gongTong)

# per = Person('wuya', 18)
# per2 = Person('lis', 20)
# # print(per.getName(),per.getAge())
# per2.setName('lisi')
# per2.setAge('25')
# print(per2.info())

# class Person(object):
# 	def __init__(self,*args,**kwargs):
# 		self.kwargs=kwargs
# 		self.args=args
#
# 	def info(self):
# 		print(u'信息:',self.args)

# per1=Person(name='wuya')
# per1.info()
#
# per2=Person(name='wuya',age=18)
# per2.info()
#
# per3=Person(name='wuya',age=18,isMarry='marry')
# per3.info()

# per4=Person('name',18,'xian')
# per4.info()


'''
首先一个类，不管是否写了构造函数，它都是有构造函数的
一个类，可以有多个构造函数,建议一个类只有一个构造函数
构造函数
1.初始化属性
'''
# class Person(object):
# 	def __init__(self,name,age):
# 		self.name=name
# 		self.age=age
#
# 	def __init__(self,address):
# 		self.address=address
#
# per=Person('xian')

'''析构函数
对象实例化-->构造函数-->对象调用方法-->代码跳转到具体的方法
-->执行方法的代码块-->最后执行析构函数
'''
# class Person(object):
# 	def __init__(self):
# 		print(u'我是构造函数')
#
# 	def __del__(self):
# 		print(u'我是析构函数')
#
# 	def info(self):
# 		print(u'我是方法')
#
# per=Person()
# per.info()

'''
普通方法
特性方法
'''
# class Person(object):
# 	def conn(self,user,passwd,host,port):
# 		pass
#
# 	def f1(self,*args,**kwargs):
# 		pass
#
# 	def info(self):
# 		print u'我是普通方法'

# per=Person()
# per.conn('root','server','localhost',3306)
# per.f1()
# per.f1('admin')
# per.f1(name='wuya')


'''
特性方法:这个方法不能有形式参数
'''
# class Person(object):
#
# 	@property
# 	def getUserID(self):
# 		pass
#
# per=Person()
# per.getUserID

# from selenium import  webdriver
# driver=webdriver.Firefox()
# driver.find_element_by_id('').text

'''
静态方法:直接使用类名来进行调用，它属于类
对象也可以调用静态方法，但是一般不建议这样做
'''
# class MySQL(object):
# 	@staticmethod
# 	def conn(user):
# 		pass
#
# # MySQL.conn('wuya')
# per=MySQL()
# per.conn('wuya')

'''
类方法:直接使用类来进行调用，属于类
'''
# class Person(object):
# 	@classmethod
# 	def conn(cls):
# 		pass

'''
属于类：
	类属性
	静态方法
	类方法
属于对象：
		实例属性
		普通方法
		特性方法
'''

'''
继承：重用已经存在的数据和行为，减少代码的重复编写
子类继承父类所有的实例变量和方法
'''

'''类属性的继承'''
# class Person(object):
# 	china=u'地球'
#
# class UsaPerson(Person):
# 	pass
#
# per=UsaPerson()
# per.china


'''实例属性的继承和继承的两种写法'''


class Fruit(object):
	def __init__(self,nanme):
		self.name=nanme


'''子类由于业务的需求，需要继承父类的实例属性'''
# class Apple(Fruit):
# 	def __init__(self,name,brand,color):
# 		# super(Apple,self).__init__(name)
# 		Fruit.__init__(self,name)
# 		self.brand=brand
# 		self.color=color
#
# 	def info(self):
# 		print u'名称{0},品牌{1},颜色{2}'.format(self.name,self.brand,self.color)
#
# apple=Apple(u'苹果',u'品牌',u'红色')
# apple.info()

'''子类由于业务的需求，不需要继承父类的实例属性'''
# class Apple(Fruit):
# 	def __init__(self,brand,color):
# 		self.brand=brand
# 		self.color=color
#
# 	def info(self):
# 		print u'品牌{0},颜色{1}'.format(self.brand,self.color)
#
# apple=Apple(u'品牌',u'红色')
# apple.info()

'''
方法的继承:
1.子类为什么重写父类的方法:子类有自己的特性
当子类重写了父类的方法后，对子类进行实例化后，子类调用的方法（父类，子类都存在），执行的方法是子类的方法


单个类继承的原则：
1.从上到下：子类继承了父类，但是子类没有重写父类的方法，那么子类实例化后，调用的方法是直接调用父类当中的方法
2.从下到上的原则:子类继承了父类，但是子类重写父类的方法，那么子类实例化后，调用的方法是子类当中的方法(子类优先考虑自己类的方法)
'''
# class Fruit(object):
# 	def eat(self):
# 		print( u'水果可以吃的')
#
# class ChinaApple(Fruit):
# 	def __init__(self,color):
# 		self.color=color
#
# 	def eat(self):
# 		print( u'颜色是{0}了的时候，可以吃'.format(self.color))
#
# class UsaApple(ChinaApple):
# 	def eat(self):
# 		print( u'我是usa的苹果')
#
# usa=UsaApple(u'红色')
# usa.eat()


# class Person(object):
# 	def __init__(self,name):
# 		self.name=name
#
# 	def info(self):
# 		print( self.name)
#
# class Son(Person):
# 	def info(self):
# 		print( self.name)
#
# s=Son('name')
# s.info()
#
'''
多个类的继承：总左到右的原则
'''
# class Person(object):
# 	def eat(self):
# 		print( u'人要吃饭')
#
# class Monther(Person):
# 	def eat(self):
# 		print( u'喜欢吃菜')
#
# class Father(Person):
# 	def eat(self):
# 		print( u'喜欢吃水果')
#
# class Son(Father,Monther):
# 	pass
#
# son=Son()
# son.eat()


# class A(object):
# 	pass
#
# class B(A):
# 	pass
#
# class C(B):
# 	pass
#
# class D(C):
# 	pass
#
# class E(C,D):
# 	pass
#
# e=E()

# class A(object):
# 	def show(self):
# 		print( 'A')
#
# class B(A):
# 	pass
#
# class C(A):
# 	def show(self):
# 		print('C')
#
# class D(B,C):
# 	pass
#
# d=D()
# d.show()

'''__doc__:打印出类的注释'''


class Person(object):
	"""对人的定义"""

	def info(self,username,password):
		'''
		获取用户的信息
		:param username:用户名
		:param password:密码
		'''
		pass


'''__call__:对象创建时直接返回__call__的内容,使用该方法可以模拟静态方法'''


class P1(object):
	def __new__(cls, *args, **kwargs):
		print('call方法')


'''
__str__:对象代表的含义，返回一个字符串,通过它可以把对象和字符串关联起来，方便某些程序的实现,
该字符串表示某个类,实现了__str__后，可以直接使用print语句输出对象,也可以通过函数str来触发__str__的执行

1.对象的意思
2.返回一个字符串，字符串和对象关联起来-->该字符串表示某个类
'''

# class Son(object):
# 	'''我是一个类'''
# 	def __str__(self):
# 		return self.__doc__
#
# s=Son()
# print str(s)


class Factory(object):
	def createFruit(self, fruit):
		if fruit == 'apple':
			return Apple()
		elif fruit == 'banana':
			return Banana()


class Fruit(object):
	def __str__(self):
		return 'fruit'


class Apple(Fruit):
	def __str__(self):
		return 'apple'


class Banana(Fruit):
	def __str__(self):
		return 'banana'


if __name__ == '__main__':
	factory = Factory()
	print(factory.createFruit('apple'))
	print(factory.createFruit('banana'))

'''工厂设计模式在UI自动化框架中的应用'''
# !/usr/bin/env python
# coding:utf-8

from appium import  webdriver
from selenium import  webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import  By


class Factory(object):
	def createWebDdriver(self, webDdriver):
		if webDdriver == 'web':
			return WebUI(self.driver)
		elif webDdriver == 'app':
			return AppUI(self.driver)


class WebDdriver(object):
	def __init__(self, driver):
		self.driver = driver

	def __str__(self):
		return 'webDdriver'

	def findElement(self, *loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException as e:
			print('Error details :%s' % (e.args[0]))

	def findsElement(self, *loc):
		try:
			return self.driver.find_elements(*loc)
		except NoSuchElementException as e:
			print('Error details :%s' % (e.args[0]))


class WebUI(WebDdriver):
	def __str__(self):
		return 'WEB UI'


class AppUI(WebDdriver):
	def __str__(self):
		return 'App UI'






