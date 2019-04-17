#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-28 10:56:23

'''
题目：删除链表中的节点

在O(1)时间内删除链表节点。给定单向链表的头指针和一个节点指针，
定义一个函数在O(1)时间内删除该节点
'''

class LinkNode:
	def __init__(self, x):
		val = x
		next = None

class Solution:
	
	def deleteNode(self, head, tobedelete):
		if not haad and not tobedelete:
			return
		# 删除结点不是链表的尾结点
		if tobedelete.next：
			tobedelete.val = tobedelete.next.val
			tobedelete.next = tobedelete.next.next
		# 链表只有一个结点
		elif head == tobedelete:
			head = None
			tobedelete = None
		# 链表结点为多个 删除链表尾结点
		# 只能从头开始遍历
		else:
			node = head
			while node.next != tobedelete:
				node = node.next

			node.next = None
		return head

'''
题目2：删除链表中重复的节点。

在一个排序的链表中，
请删除重复的节点，
如1-2-3-3-4-4-5在重复的节点被删除后为1-2-5。
思路：
运用链表的操作，确保将重复的节点略过，始终连接不重复的值。
'''
class Solution:
	def deleteDuplication(self, head):
		first = LinkNode(-1)
		first.next = head
		last = head

		while head and head.next:
			if head.val == head.next.val:
				val = head.val
				while head and head.val == val:
					head = head.next
				last.next = head
			else:
				last = head
				head = head.next
		return first.next


