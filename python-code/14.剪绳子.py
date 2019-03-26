#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-26 16:10:15

'''
题目：剪绳子
给你一根长度为n的绳子，请把绳子剪成m段
(m,n都是整数，且n>1,m>1),
每段绳子的长度记为k[0],k[1],k[2],...,k[m]。
请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
例如，当绳子的长度为8时，我们把它剪成长度分别为2，3，3的三段，
此时得到的最大乘积为18
'''

class Solution:
	# 动态规划
	# 状态转移方程：f(n)=max(f(i)*f(n-i))
	def maxProductAfterCutting_solution(length):
		if length < 2:
			return 0
		elif length == 2:
			return 1
		elif length == 3:
			return 2
		products = [0, 1, 2, 3]

		max_ = 0

		for i in range(length+1):
			max_ = 0
			for j in range(1, i/2):
				product = products[j] * products[i-j]
				max_ = product if max_ < product else max_
			products[i].append(max_)
		returm products[-1]

	# 贪心算法
	# 当n >= 5时 尽可能的多剪长度为3的绳子，当剩下绳子长度为4时，剪成2+2 这种策略乘积将最大
	def maxProductAfterCutting_solution2(length):
		if length < 2:
			return 0
		elif length == 2:
			return 1
		elif length == 3:
			return 2
		timeOf3 = length / 3
		if length % 3 == 1:
			timeOf3 -= 1
		timeOf2 = (length - timeOf3 * 3) / 2
		return pow(3, timeOf3) * pow(2, timeOf2)
		
