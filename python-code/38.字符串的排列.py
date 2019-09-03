#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

解题思路：把字符串看成两部分：第一部分是它的第一个字符；第二部分是后面的所有字符。 递归
'''

class Solution:
    def permulation(self, string):
        if not string:
            return

        res = []
        for i in range(len(string)):
            if i > 0 and string[i] == string[i-1]:
                continue
            temp = self.permulation(string[:i] + string[i+1:])
            for j in temp:
                res.append(string[i]+j)

        return res


