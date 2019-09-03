#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题：输入一个复杂链表（每个节点中有节点值，以及两个指针，
一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
(注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空)
'''

class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.sibling = None

class Solution:

    def cloneNodes(phead):
        pnode = phead
        while pnode:
            pchone = new LinkNode(pnode.val)
            pchone.next = pnode.next
            pchone.sibling = None

            pnode.next = pchone
            pnode = pchone.next

    def connectSiblingNodes(phead):
        pnode = phead
        while pnode:
            pchone = pnode.next
            if pnode.sibling:
                pchone.sibling = pnode.sibling.next
            pnode = pchone.next


    def reconnectNodes(phead):
        pnode = phead
        pchnoehead = None
        pchonenode = None

        if pnode:
            pchnoehead = pchonenode = pnode.next
            pnode.next = pchonenode.next
            pnode = pnode.next

        while pnode:
            pchonenode.next = pnode.next
            pchonenode = pchonenode.next

            pnode.next = pchonenode.next
            pnode = pnode.next

        return pchnoehead


    def clone(phead):
        cloneNodes(phead)
        connectSiblingNodes(phead)
        reconnectNodes(phead)






