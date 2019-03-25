#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-08 10:38:07

'''
第二章：面试需要的基础知识
2.3 数据结构
面试题3：数组中重复的数字
题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2
'''

'''
思路1：输入数组排序 再遍历
时间复杂度：O(nlogn)
'''
def Solution_one(list_data):
	if len(list_data) <= 1:
		return list_data
	sort_data = mergeSort(list_data)
	# sort_data = sorted(list_data)
	res = []
	i = 0
	while i < len(sort_data)-1:
		if sort_data[i] == sort_data[i+1]:
			res.append(sort_data[i])
		i += 1
	return set(res)

# 归并排序
def mergeSort(lists):
	if len(lists) <= 1:
		return lists
	mid = len(lists) // 2
	left = mergeSort(lists[:mid])
	right = mergeSort(lists[mid:])
	return merge(left, right)

# 归并算法
def merge(left, right):
	r = l = 0
	res = []
	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			res.append(left[l])
			l += 1
		else:
			res.append(right[r])
			r += 1
	res += left[l:] + right[r:]
	return res

'''
思路2：哈希表
时间复杂度：O(n)
空间复杂度：O(n)
'''
import collections
def Solution_two(list_data):
	res = []
	dict_data = collections.defaultdict(int)
	for data in enumerate(list_data):
		val = dict_data.get(0, data)
		if not val:
			res.append(res)
		dict_data[data] = val + 1
	return res
