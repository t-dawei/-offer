#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题：不分行从上到下打印二叉树
'''

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def printFormTopToBottom(root):

        if not root:
            return 
            
        res_root = [root]
        results = []
        while res_root:
            root = res_root.pop[0]
            results.append(root.val)
            if not root.left:
                res_root.append(root.left)
            if not root.right:
                res_root.append(root.right)

        return results

