#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题目：
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。

解题思路一：
由于输入的一个二叉搜索树，其左子树不大于右子树的值，这位后面的排序做了准备，
因为只需要中序遍历即可，将所有的节点保存到一个列表，。
对这个list[:-1]进行遍历，每个节点的right设为下一个节点，下一个节点的left设为上一个节点。

借助了一个O（n）的辅助空间 
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    self.attr = []

    def conver(self, root):
        if not root:
            return
        self.inorder(root)

        for i, val in enumerate(self.attr[:-1]):
            self.attr[i].right = self.attr[i+1]
            self.attr[i+1].left = val

        return self.attr[0]

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.append(root)
        self.inorder(root.right)

