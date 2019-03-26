#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-26 09:19:00

'''
题目：
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项。
n<=39
n=0时，f(n)=0 n=1时，f(n)=1 n>1时，f(n)=f(n-1)+f(n-2)
'''

class Solution:
	# 递归方法
	def Fibonacci(self, n):
		if n <= 0:
			return 0
		elif n == 1:
			return 1
		return Fibonacci(n-1) + Fibonacci(n-2)

	# 循环方法
	def Fibonacci2(self, n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		one, two = 1, 0
		for i in range(2, n+1):
			sum = one + two
			two = one
			one = sum
		# 在python中只有模块，类，和函数才会产生新的作用域，所以for循环里定义的变量在循环外也能访问，只要他们在同一个作用域里
		return sum

