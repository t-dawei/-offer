#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-26 20:15:39

'''
题目：二进制中1的个数
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

class Solution:
	# 当n只能为正整数
	def NumberOf1(self, n):
		count = 0
		while n:
			if n & 1:
				count += 1
			n = n >> 1
		return count

	# 常规解法 适用于整数
	# 循环的次数等于二进制的位数
	def NumberOf1_2(self, n):
		count, flag = 0, 1
		while flag:
			if n & flag:
				count += 1
			flag = flag << 1
		return count

	# 最佳解法
	# 循环的次数等于二进制中1的个数
	# 把一个整数减去1 在和原来整数做与运算，会吧最右边的1变成0
	def NUmberOf1_3(self, n):
		count = 0
		while n:
			count　+= 1
			n = (n - 1) & n
		return count