#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-26 11:23:38

'''
题目：矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中
向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如 
a b c e 
s f c s 
a d e e 
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
路径不能再次进入该格子。
'''

class Solution:
    # 回溯+递归
    def hasPath(self, matrix, rows, cols, str):
        if not matrix or rows < 0 or cols < 0 or not str:
            return False

        visited = [[0 for i in range(cols)] for j in range(rows)]
        s_index = 0

        for r in range(rows):
            for c in range(cols):
                if hasPathCore(self, matrix, rows, cols, str, s_index, visited, r, c):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, str, s_index, visited, r, c):
        if s_index == len(str):
            return True

        hasPath = False
        if 0 < r < rows and 0 < c < cols and matrix[r][c] == str[s_index] and not visited[r][c]:
            s_index += 1
            visited[r][c] = 1

            hasPath = hasPathCore(self, matrix, rows, cols, str, s_index, visited, r, c+1) or \
                      hasPathCore(self, matrix, rows, cols, str, s_index, visited, r, c-1) or \
                      hasPathCore(self, matrix, rows, cols, str, s_index, visited, r+1, c) or \
                      hasPathCore(self, matrix, rows, cols, str, s_index, visited, r-1, c)
            if not hasPath:
                s_index -= 1
                visited[r][c] = 0

        return False