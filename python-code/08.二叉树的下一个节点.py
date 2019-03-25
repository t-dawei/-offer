#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-25 15:07:45

'''
题目：二叉树的下一个节点

题目描述：
给定一个二叉树和其中的一个结点，
请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，
同时包含指向父结点的指针。
'''
'''
思路：
1. 如果一个结点有右子树，那么他的下一个结点就是它的右子树中的最左子节点
2. 如果一个结点没有右子树，而且他是他父节点的左节点，那么他的下一个结点就是它的父节点
3. 如果一个结点没有右子树，而且他是他父节点的右节点，那么沿着指向父节点的指针一直向上遍历，
	直到找到一个是他父节点的左子结点的节点。
'''
class Treenode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        self.pre = None

class Solution:
    def nextNode(self, pNode):
        if not pNode:
            return
        elif pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        elif pNode.right and pNode.pre.left is pNode:
            return pNode.pre
        else:
            while pNode.pre and pNode.pre.left is not pNode:
                pNode = pNode.pre
            return pNode.pre


