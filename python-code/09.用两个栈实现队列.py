#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-25 15:57:13

'''
题目描述：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

解题思路：
有两个栈stackA,stackB，A为入栈，B为出栈的。
入栈时，直接进入A即可，出栈时，先判断B中是否有元素，
如果没有肯定不能pop()，
应将A中所有元素倒压在B里面，再pop()最上面（后面）的元素，
如果有，直接pop()就可以了。
两个栈各自先进后出，在一起又实现了队列的新进先出。
'''

class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x):
        self.stackA.append(x)

    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()

