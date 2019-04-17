#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-28 15:17:16

'''
题目：正则表达式匹配
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
'''

class Solution:
	def match(self, s, pattern):
		if not s and not pattern:
			return True
		if s and not pattern:
			return False

		# 当模式中的第二个字符是*时
		if len(pattern) > 1 and pattern[2] == '*':
			# 如果字符串第一个模式跟模式第一个字符匹配时，可以有三种匹配方式
			if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
				return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
			else:
				return self.match(s, pattern[2:])

		# 当模式中的第二个字符不是*时
		# 如果字符串第一个字符和模式第一个字符匹配时
		if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
			return self.match(s[1:], pattern[1:])
		return False
