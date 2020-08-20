#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/18 11:46 下午
# @Author : xiongtao
# @File : 01.07_Rotate.py

'''
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
不占用额外内存空间能否做到？
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

官方题解：https://leetcode-cn.com/problems/rotate-matrix-lcci/solution/xuan-zhuan-ju-zhen-by-leetcode-solution/
'''


class Rotate():
    def rotate(self, matrix):
        n = len(matrix)
        row = len(matrix)//2
        col = (len(matrix)+1)//2
        for i in range(0, row):
            for j in range(0, col):
                matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1] = matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]
        return matrix


if __name__ == '__main__':
    R = Rotate()
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    print(R.rotate(matrix))