#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题目：如果一个链表中包含环，如何找出环的入口节点？

解题分析：其实此题可以分解为三个题目：
1）如何判断一个链表中是否包含环？
2）如何找到环的入口节点？
3）如何得到环中节点的数目？

解决此题：可以设置两个指针，一快一慢。

1.两个指针一个fast、一个slow同时从一个链表的头部出发
  fast一次走2步，slow一次走一步，如果该链表有环，两个指针必然在环内相遇，
 （如果相遇就证明此链表包含环，否则没有环，解决问题1）
2.此时只需要把其中的一个指针重新指向链表头部，另一个不变（还在环内），
  这次两个指针一次走一步，相遇的地方就是入口节点（解决问题2，得到环的入口节点）。
2.接着步骤1，如果两个指针相遇，必然在环内，所以可以从这个节点出发，一遍继续向前移动，一遍计数，
  当再次回到这个节点时，就可以得到环中节点数了（解决问题3，得到环中节点数目）
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# 判断是否存在环 并返回环的入口点
class Solution:
	def entryNodeOfLoop(self, phaead):
		pfast = pslow = phaead
		while pfast != None and pfast.next != None:
			pfast = pfast.next.next
			pslow = pslow.next
			if pfast == pslow:
				break
		if pfast == None or pfast.next == None:
			return None
		pfast = phaead
		while pfast != pslow:
			pfast = pfast.next
			pslow = pslow.next
		return pfast 

# 计算环中的节点
class Solution:
	def entryNodeOfLoop(self, phaead):
		pfast = pslow = phaead
		while pfast != None and pfast.next != None:
			pfast = pfast.next.next
			pslow = pslow.next
			if pfast == pslow:
				break
		if pfast == None or pfast.next == None:
			return None
		meetingNode = pfast
		nodeInlooop = 1 
		while pfast.next != meetingNode:
			pfast = pfast.next
			nodeInlooop += 1 
		return nodeInlooop



















