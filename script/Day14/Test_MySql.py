# !/usr/bin/python3
# coding:utf-8
# author:panli
import pymysql


def connMySql():
	try:
		con = pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='root',
			database='five')

	except Exception as e:
		return e.args

	else:
		cur = con.cursor()
		# sql = ' select * from user where id=%s'
		# params = (1,)
		# cur.execute(sql, params)
		# 代表单查询，只查询一个数据
		# data = cur.fetchone()
		# print(data)
		cur.execute('select * from user')
		# 如果想要查询多行的话，使用cur.fetchall()
		data2 = cur.fetchall()
		result = [items for items in data2]
		print(result)
	finally:
		cur.close()
		con.close()


def test_Insert():
	try:
		con = pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='root',
			database='five')

	except Exception as e:
		return e.args

	else:
		cur = con.cursor()
		# 单条语句的插入
		# sql = ' insert into user values(%s, %s, %s, %s)'
		# params = (3, 'xiaoming', '20', 'BJ')
		# cur.execute(sql, params)
		# con.commit()
		# 多条语句插入
		sql = ' insert into user values(%s, %s, %s, %s)'
		params = [
			(4, 'wangyuan', '22', 'SZ'),
			(5, '王俊凯', '23', 'HN'),
			(6, '王凯', '24', 'AH')
			]
		cur.executemany(sql, params)
		con.commit()

	finally:
		cur.close()
		con.close()


def Delete_MySql():
	try:
		con = pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='root',
			database='five')

	except Exception as e:
		return e.args

	else:
		cur = con.cursor()
		# 删除语句
		sql = ' delete from  user where id =%s '
		params = (5,)
		cur.execute(sql, params)
		con.commit()

	finally:
		cur.close()
		con.close()


class MySql_Helder():
	def conn(self):
		conn = self.conn = pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='root',
			db='five'
		)
		return conn

	def get_Query(self, sql, params):
		cur = self.conn().cursor()
		cur.execute(sql, params)
		result = cur.fetchone()
		return result


def Checkvalue(address, name):
	opera = MySql_Helder()
	sql ='select * from user where address=%s and name=%s '
	params = (address, name)
	return opera.get_Query(sql=sql, params=params)


def info():
	name = input('请输入您的姓名：\n')
	address = input('请输入您的地址：\n')
	result1 = Checkvalue(address=address, name=name)
	if result1:
		print('你好，{0}！恭喜你登陆成功'.format(name))

	else:
		print('登陆失败')
		info()


if __name__ == '__main__':
	info()



