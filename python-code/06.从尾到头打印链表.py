#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-25 10:52:40

class LinkNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    # 使用栈结构
    def printLink(self, head):
        list_res = res
        cur = head
        while cur is not None:
            list_res.append(cur.val)
            cur = cur.next
        return list_res[::-1]

    # 使用递归
    def printLink2(self, head):
        if head is not None:
            printLink(head.next)
            prin(head.val)

