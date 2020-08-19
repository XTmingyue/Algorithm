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
'''

class Rotate():
    def rotate(self, matrix):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):

        return []


if __name__ == '__main__':
    R = Rotate()
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    print(R.rotate(matrix))