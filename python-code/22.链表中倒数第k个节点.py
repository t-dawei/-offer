#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题：输入一个链表，输出该链表中倒数第k个结点。

解题思路：
	为了实现只遍历链表一次就能找到倒数第k个节点，我们可以定义两个指针。
	让第一个指针先向前走k-1步，第二个指针保持不动；
	从第k步开始，第二个指针也开始从链表的头指针开始遍历。
	由于两个指针的距离保持在k-1,
	当第一个指针到达链表的尾节点时，
	第二个指针刚好到达倒数第k个节点。

'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def FindKthToTail(self, head, k):
		if not head or k <= 0:
			return None
		pquick = head
		for i in range(k-1):
			if pquick.next:
				pquick = pquick.next
			else:
				return None
		pslow = head
		while pquick.next:
			pquick = pquick.next
			pslow = pslow.next
		return pslow


