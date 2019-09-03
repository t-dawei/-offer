#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题目：请实现两个函数，分别用来序列化和反序列化二叉树

解题思路：
首先来看二叉树的序列化，二叉树的序列化就是采用前序遍历二叉树输出节点，
再碰到左子节点或者右子节点为None的时候输出一个特殊字符”#”。
对于反序列化，就是针对输入的一个序列构建一棵二叉树，我们可以设置一个指针先指向序列的最开始，
然后把指针指向位置的数字转化为二叉树的结点，后移一个数字，继续转化为左子树和右子树。
当遇到当前指向的字符为特殊字符”#”或者指针超出了序列的长度，则返回None，指针后移，继续遍历。
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None


class Solution:
    self.stream = []
    self.index = -1
    def serialize(self, root):
        if not root:
            self.stream.appenp('$')

        self.stream.append(root.val)
        self.serialize(root.left)
        self.serialize(root.right)

    def deserialize(self):
        self.index += 1
        root = None
        if self.stream[index] != '$':
            root = TreeNode(self.stream[index])
            root.left = deserialize(root.left)
            root.right = deserialize(root.right)
        return root


