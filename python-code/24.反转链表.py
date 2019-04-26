#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题：输入一个链表，反转链表并输出反转后链表的头节点。

解题思路：注意反转时出现断裂现象，定义3个指针，分别指向当前遍历到的节点pNode、它的前一个节点pPrev及后一个节点pNext。
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def reverseList(self, phead):
		pre, pnode, pnext = None, phead, None
		while pnode:
			pnext = pnode.next
			pnode.next = pre 
			pre = pnode
			pnode = pnext
		return pre 
		