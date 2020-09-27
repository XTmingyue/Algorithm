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
参考求 084 最大矩形 的求解方案。
以每一行为地基，计算在地基上的柱形构成的最大矩形
'''
class MaxRectangle:
    # 采用暴力剪枝的方法进行求解
    def maxRectangleSub(self, nums):
        max_Area = 0
        for i in range(len(nums)):
            # 只有遇到峰值才进行计算
            if (i < len(nums) - 1 and nums[i] > nums[i + 1]) or i == len(nums) - 1:
                min_len = nums[i]
                # 往前遍历计算面积
                for j in range(i, -1, -1):
                    min_len = min(min_len, nums[j])
                    max_Area = max(max_Area, min_len * (i - j + 1))
        return max_Area

    def maxRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        # 计算每个地基上的柱形高度
        row, col = len(matrix), len(matrix[0])
        A = [[0] * col for _ in range(row)]
        for j in range(col):
            cum_num = 0
            for i in range(row):
                if matrix[i][j] == "1":
                    cum_num += 1
                else:
                    cum_num = 0
                A[i][j] = cum_num
        max_Area = 0
        # 计算以每一行为地基时，地基之上的柱形围成的最大矩形
        for i in range(row):
            max_Area = max(max_Area, self.maxRectangleSub(A[i]))
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