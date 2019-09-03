#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def findPath(root, experctedSum):
        if not root:
            return
        path = []

        self.findPathCore(root, path, experctedSum, 0)


    def findPathCore(root, path, experctedSum, curSum):
        path.append(root)
        curSum += root.val
        if not root.left and not root.right and curSum == experctedSum:
            for node in path:
                print(node.val)

        if curSum < experctedSum:
            if root.left:
                self.findPathCore(root.left, path, experctedSum, curSum)
            if root.right:
                self.findPathCore(root.right, path, experctedSum, curSum)

        path.pop()
    




