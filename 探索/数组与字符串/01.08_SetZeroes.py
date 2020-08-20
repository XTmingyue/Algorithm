#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/19 11:33 下午
# @Author : xiongtao
# @File : 01.08_SetZeroes.py

'''
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
'''

class SetZeros():
    def setZeros(self, matrix):
        if len(matrix)==0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        empty_rows = set()
        empty_cols = set()
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    empty_rows.add(i)
                    empty_cols.add(j)
        for row in empty_rows:
            for i in range(0, n):
                matrix[row][i] = 0
        for col in empty_cols:
            for i in range(0, m):
                matrix[i][col] = 0
        return matrix

if __name__ == '__main__':
    ST = SetZeros()
    matrix = [[1,1,1],
              [1,0,1],
              [1,1,1]]
    print(ST.setZeros(matrix))