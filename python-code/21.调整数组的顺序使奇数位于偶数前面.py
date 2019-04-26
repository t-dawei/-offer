#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题一：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

解题思路：使用两个指针，第一个指针初始化指向数组的第一个数字，从前向后移动，
遇到偶数就停下来；第二个指针指向数组的最后一个数字，从后向前移动，
遇到奇数就停下来，交换两个指针指向的元素，直到两个指针相遇。
'''

class Solution:
	def reOrderArray(self, array):
		if not array:
			return
		phead, ptail = 0, len(array) - 1

		while phead < ptail:
			while phead < ptail and array[phead] & 1 == 1:
				phead += 1
			while phead < ptail and array[ptail] & 1 == 0:
				ptail -= 1
			if phead != ptail:
				array[phead] = array[ptail]
		return array


