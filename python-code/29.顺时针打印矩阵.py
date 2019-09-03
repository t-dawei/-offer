#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

'''
题目：顺时针打印矩阵（同LeetCode 螺旋矩阵打印）

题：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
'''

class Solution:
    def printMatrix(self, matrix, rows, column):
        if not matrix or rows <= 0 or column <= 0:
            return

        start = 0
        while column > start * 2 and rows > start * 2
            printMatrixInCircle(matrix, rows, column, start)
            start += 1

		

    def printMatrixInCircle(self, matrix, rows, column, start, res):
        endx = column - start - 1
        endy = rows - start - 1
        for i in range(start, endx+1):
            print(matrix[start][i])
        if start < endy:
            for i in range(start+1, endy+1):
                print(matrix[i][endx])
        if start < endx and start < endy:
            for i in range(endy-1, start):
                print(matrix[endy][i])
        if start < endy and start < endy-1:
            for i in range(endy-1, start+1):
                print(matrix[i][start])
