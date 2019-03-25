#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-25 09:55:25

'''
题目：
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

class Solution:
    # 使用join方法
    def replaceSpace(self, string):
        return '%20'.join(string.split(' '))

    # 使用replace方法
    def replaceSpace2(self, string):
        return string.replace(' ', '%20')

    # 剑指offer双指针移动赋值法
    def replaceSpace3(self, string):
        new_s = list(string + ' ' * (string.count(' ') * 2))
        print(new_s)
        p1 = len(string)-1
        p2 = len(new_s)-1
        while p1 >= 0:
            if new_s[p1] == ' ':
                for i in ['0', '2', '%']:
                    new_s[p2] = i
                    p2 -= 1
            else:
                new_s[p2] = new_s[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(new_s)

if __name__ == '__main__':
    string = 'We are happy '
    print(Solution().replaceSpace3(string))