#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/22 8:42 上午
# @Author : xiongtao
# @File : 085_MaximalRectangle.py 
# @Title : 85. 最大矩形

'''
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
'''

'''
题解：
定义数组row[i][j]：表示在row[i]行中，以matrix[i][j]为最后一个元素的连续1的个数
定义数组A[i][j]:表示以matrix[i][j]为右下角的最大的矩形面积。如何求呢？
    我们只需要确定截止第j列，从行i以上最小的连续1的个数，就能计算出不同矩形的面积，取其中的最大值。
'''
class MaxRectangle:
    def maxRectangle(self, matrix):
        if len(matrix) <= 0:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        # 初始化两个数组
        row = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            # 累计1的个数
            cum_num = 0
            for j in range(cols):
                if matrix[i][j] == "1":
                    cum_num += 1
                else:
                    cum_num = 0
                row[i][j] = cum_num

        max_Area = 0
        for i in range(rows):
            for j in range(cols):
                min_num = cols
                for k in range(i, -1, -1):
                    min_num = min(min_num, row[k][j])
                    max_Area = max(max_Area, min_num * (i - k + 1))
        return max_Area

    # 合并两个循环
    def maxRectangle_2(self, matrix):
        if len(matrix) <= 0:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        # 初始化两个数组
        row = [[0] * cols for _ in range(rows)]
        max_Area = 0
        for i in range(rows):
            # 累计1的个数
            cum_num = 0
            for j in range(cols):
                # 计算累计1的个数
                if matrix[i][j] == "1":
                    cum_num += 1
                else:
                    cum_num = 0
                row[i][j] = cum_num
                # 计算最大面积
                min_num = cols
                for k in range(i, -1, -1):
                    min_num = min(min_num, row[k][j])
                    max_Area = max(max_Area, min_num * (i - k + 1))
        return max_Area

if __name__ == '__main__':
    class_MR = MaxRectangle()
    matrix = [
              ["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]
            ]
    print(class_MR.maxRectangle(matrix))