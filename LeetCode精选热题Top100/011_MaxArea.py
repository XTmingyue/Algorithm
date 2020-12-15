#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/11/9 8:37 上午
# @Author : xiongtao
# @File : 011_MaxArea.py 
# @Title : 11. 盛最多水的容器

'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
'''

class MaxArea:
    def maxArea(self, height):
        n = len(height)
        if n <= 1:
            return 0
        start = 0
        end = n - 1
        max_Area = 0
        while start < end:
            curr_min = min(height[start], height[end])
            max_Area = max(max_Area, (end - start) * curr_min)
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return max_Area


if __name__ == '__main__':
    MA = MaxArea()
    height = [1,8,6,2,5,4,8,3,7]
    print(MA.maxArea(height))