#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-26 15:15:57

'''
题目：机器人的运动范围
地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？
'''

class Solution:
    # 回溯+递归
    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        visited = [[0 for i in range(cols)] for j in range(rows)]
        count = self.movingCountCore(self, threshold, rows, cols, 0, 0, visited)
        return count

    def movingCountCore(self, threshold, rows, cols, r, c, visited):
        count = 0
        if check(threshold, rows, cols, r, c, visited):
            visited[c][c] = 1
            count = 1 + self.movingCountCore(threshold, rows, cols, r, c+1, visited) + \
                self.movingCountCore(threshold, rows, cols, r, c-1, visited) + \
                self.movingCountCore(threshold, rows, cols, r+1, c, visited) + \
                self.movingCountCore(threshold, rows, cols, r-1, c, visited)
        return count

    def check(self, threshold, rows, cols, r, c, visited):
        if 0 <= c < cols and 0 <= r <rows and (self.getDigitNum(r) + self.getDigitNum(c)) <= threshold and not visited[r][c]:
            return True
        else:
            return False

    def getDigitNum(self, number):
        return sum(list(map(int, list(str(number)))))
