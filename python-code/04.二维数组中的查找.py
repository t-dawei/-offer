#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-25 09:16:37

'''
题目：
在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

# 从二维数组的右上角或者左下角开始去除列和边
class Solution:
	def find(self, array, target):
		row, col = len(array), len(array[0])
		i, j = 0, col-1
		while i < row and j >= 0:
			if array[i][j] < target:
				i += 1
			elif array[i][j] > target:
				col -= 1
			else:
				return True
		return False

# test
if __name__ == '__main__':

	array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
	target = 7
	print(Solution.find(array, 7))