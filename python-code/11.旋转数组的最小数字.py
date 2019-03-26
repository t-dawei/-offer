#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-26 10:26:02

'''
题目：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0
'''

class Solution:
	# 二分查找
	def Mindata(self, data):
		if not data:
			return 0
		head, tail, mid = 0, len(data)-1, 0
		while data[head] >= data[tail]:
			if head - tail == 1:
				mid = tail
				break
			mid = (head + tail) / 2
			if data[head] == data[tai] == data[mid]:
				# 只能顺序查找
				return min(data)
			if data[mid] >= data[head]:
				head = mid
			elif data[mid] <= data[tail]:
				tail = mid
		return data[mid]
