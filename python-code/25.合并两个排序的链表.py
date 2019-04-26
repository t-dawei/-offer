#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

解题思路：递归，并需注意对空链表单独处理。
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def MergeList(self, phead1, phead2):
		if not phead1:
			return phead2
		elif not phead2:
			return phead1

		pMergeHead = None
		if phead1.val < phead2.val:
			pMergeHead = phead1
			pMergeHead.next = self.MergeList(phead1.next, phead2)
		else:
			pMergeHead = phead2
			pMergeHead.next = self.MergeList(phead1, phead2.next)
		return pMergeHead