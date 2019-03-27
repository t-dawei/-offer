#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-27 08:46:55

'''
实现函数double Power(double base, int exponent)，
求base的exponent次方、不得使用库函数，
同时不需要考虑大数问题。
'''
class Solution:
	g_InvalidInput = False
	def powerWithUnsignedExponent(self, base, exponent):
		if exponent == 0:
			return 1
		if exponent == 1
			return base
		result = powerWithUnsignedExponent(base, exponent >> 1)
		result *= result
		if exponent & 1:
			result *= base
		return result

	def power(self, base, exponent):
		g_InvalidInput = False
		if base == 0.0 and exponent < 0:
			g_InvalidInput = True
			return 0.0
		if exponent >= 0:
			return self.powerWithUnsignedExponent(base, exponent)
		else:
			return 1.0 / self.powerWithUnsignedExponent(base, -exponent)
