#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题：输入两棵二叉树A和B，判断B是不是A的子结构。

解题思路：递归，注意空指针的情况。
'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def HasSubtree(self, proot1, proot2):
		res = False
		if proot1 and proot2:
			if proot1.val == proot2.val:
				res = self.subtreeCore(proot1, proot2)
			if not res:
				res = self.HasSubtree(proot1.left, proot2)
			if not res:
				res = self.HasSubtree((proot1.right, proot2))
		return res

	def subtreeCore(self, proot1, proot2):
		if proot2 == None:
			return True
		if proot1 == None:
			return False
		if proot1.val != proot2.val:
			return False
		return self.subtreeCore(proot1.left, proot2.left) and self.subtreeCore(proot1.right, proot2.right)

