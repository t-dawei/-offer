#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的

解题思路：

可以定义一种遍历算法，先遍历右子节点再遍历左子节点。注意，我们必须把遍历二叉树时遇到的空指针考虑进来。
'''

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSymmetrical(self, proot):
		self.isSymmetricalCore(proot, proot)

	def isSymmetricalCore(self, proot1, proot2):
		if not proot1 and not proot2:
			return True
		if not proot1 or not proot2:
			return False
		if proot1.val != proot2.val:
			return False
		return self.isSymmetricalCore(proot1.left, proot2.right) and self.isSymmetricalCore((proot1.right, proot2.left))