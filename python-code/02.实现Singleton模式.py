#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-07 18:25:13

'''
第二章：面试需要的基础知识
2.2 编程语言
面试题2：实现Singleton模式
题目：设计一个类，我们只能生成该类的一个实例
'''

# 导入线程安全库
import threading

class Singleton(object):

	# 实例化一个线程锁
	instance_lock = threading.Lock()

	# 实例初始化函数
	def __init__(self):
		pass

	# 对象创建函数
	'''
	加锁是非常耗时的操作
	可行办法：加同步锁前后两次判断实例是否已经存在
	'''
	def __new__(cls, *args, **kwargs):
		if not hasattr(Singleton, '_instance'):
			with Singleton.instance_lock:
				if not hasattr(Singleton, '_instance'):
					Singleton._instance = object.__new__(cls)
		return Singleton._instance


'''
测试
'''
def task(args):
	obj = Singleton()
	print(id(obj))

for i in range(10):
	t = threading.Thread(target=task, args=[i,])
	t.start()
