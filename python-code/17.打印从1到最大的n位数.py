#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-27 09:43:28

'''
输入数字n,
按顺序打印出从1到最大的n位十进制数，
比如输入3，则打印出1、2、3一直到最大的3位数999
'''

class Solution:

    # 排列组合解法 用递归实现
    def print1toMaxOfNdigits(self, n):
    	if n <= 0:
    		return
    	number = [0 for i in range(n)]

    	for i in range(10):
    		number[0] = i
    		print1ToMaxOfNDigitsRecursively(n, 0)

    def print1ToMaxOfNDigitsRecursively(self, n, index):
    	if index == (n - 1):
    		printNumber(number)
    	for i in range(10):
    		number[index + 1] = i 
    		print1ToMaxOfNDigitsRecursively(n, index+1)

    def printNumber(number):
    	return int(''.join(map(str, number)))