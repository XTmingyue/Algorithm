#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/23 8:43 上午
# @Author : xiongtao
# @File : 084_LargestRectangleArea.py 
# @Title : 84. 柱状图中最大的矩形

'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

输入: [2,1,5,6,2,3]
输出: 10
'''

'''
题解：
遍历整个数组heights，计算以heights[i]为右边界的最大面积。

暴力方法：
    1. 对于每个heights[i]，从i开始遍历i之前的元素j，计算[j,i]之间的面积（最小高度*宽度）；
    2. 保留每次计算的最大面积。时间复杂度O(n^2)
修改暴力方法：
    1. 我们没有必要对每个heights[i]都计算一次，只需要对每次递增的峰值进行计算即可（峰值就是比右边元素大的值）；
    2. 原因是因为，若元素a[i]是峰值，即a[i] >= a[i-1]，那么以a[i]为右边界的最大面积 >= 以a[i-1]为右边界的最大面积；

'''

class LargestRectangleArea:
    # 修改的暴力方法
    def largestRectangleArea(self, heights):
        max_Area = 0
        for i in range(len(heights)):
            # 确定是否是峰值
            if (i < len(heights) - 1 and heights[i] > heights[i + 1]) or i == len(heights) - 1:
                # 计算以i为右边界的最大面积
                min_num = heights[i]
                for j in range(i, -1, -1):
                    # 计算[j,i]之间的最小值
                    min_num = min(min_num, heights[j])
                    max_Area = max(max_Area, min_num * (i - j + 1))
        return max_Area

if __name__ == '__main__':
    class_LRA = LargestRectangleArea()
    heights = [2,1,5,6,2,3]
    print(class_LRA.largestRectangleArea(heights))