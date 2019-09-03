#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。

解题思路：递归
'''

class Solution:
    def verifySquenceOfBST(sequence):
        if not sequence:
            return

        root_val = sequence[-1]

        for index, val in enumerate(sequence):
            if val > root_val:
                break

        for i in range(index, len(sequence)-1):
            if sequence[i] < root:
                return False

        if index > 0:
            left = verifySquenceOfBST(sequence[:index])
        if index < len(sequence)-1:
            right = verifySquenceOfBST(sequence[index:])

        return left and right

