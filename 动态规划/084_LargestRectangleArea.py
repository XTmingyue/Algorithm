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

'''
单调栈的
对于数组中的某一个元素nums[i]，我们想计算以nums[i]为高度的矩形最大面积，那么就需要计算以nums[i]为高度的矩形的最大宽度。

要计算最大宽度就需要知道以nums[i]为高度的矩形的左右边界。先不说左边界，先明确如何确定右边界。
如果nums[i+1]<nums[i]，那么nums[i]的右边界就是nums[i+1]。
由此我们知道在对数组nums进行遍历过程中，只要遇到nums[i+1]<nums[i]，那么此时就可以确定i+1前面某些大于nums[i+1]高度的矩阵的右边界。

而对于遍历过程中那些不能确定右边界的元素，我们用数组A将其按顺序存起来，那么数组中元素对应的高度一定是单调递增的。
因为如果不是单调的，那么一定存在A[i]>A[i+1]，此时我们是可以确定A[i]的右边界就是A[i+1]，与数组A的定义矛盾了。
对于数组A，假设数组最后一个元素是nums[i]，那么当num[i+1]<nums[i]时，我们就至少可以确定nums[i]的右边界，
就需要将nums[i]移除数组A并计算此时nums[i]的左边界，得到以nums[i]为高度的最大矩阵面积。
并且我们还要继续取数组深剩余元素中最后一个元素与num[i+1]比较，如果还是大于nums[i+1]，那么我们继续移出数组计算面积，
直到数组中最后一个元素的值小于nums[i+1]（此时就不能确定右边界）或者为空，那么我们将nums[i+1]加入到数组中。

这个时候大家就会问，上面你只求了右边界，还没说怎么求左边界呢，没有左边界怎么算矩形的面积？
其实在上面的递增数组中就已经有了A[i]的左边界了，我们知道数组A是单调递增的，A[i-1] < A[i]，那么对于A[i]对应的元素的左边界就是A[i-1]

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