#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-28 16:03:19

'''
题目：表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
解题思路：
	利用python中国=的float强转 如果可以那么它是一个合法的数值字符串，否则不是
'''

class Solution:
	def isNumer(self, s):
		try:
			return float(s)
		except:
			retun 0
			
