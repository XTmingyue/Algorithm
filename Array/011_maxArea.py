#!/usr/bin python
# -*- coding: utf-8 -*- 

# @Time : 2020/7/2 7:57 PM 
# @Author : xiongtao
# @File : 011_maxArea.py

'''
题目：给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

输入：[1,8,6,2,5,4,8,3,7]
输出：49
'''

class MaxArea():
    '''
    解法1：双指针法，i从0开始移动，j从len(height)开始移动，每次只移动一边的指针。
    假设s(i,j)表示height[i]与height[j]之间的面积，要想移动一边的指针使得面积可能变大，那么只能移动i和j中最短的边
    因为移动最长的边并不会使得最短的边增大，而面积的大小取决于最短的边。

    时间复杂度:O(N)
    '''
    def max_Area(self, height):
        maxArea = 0
        left = 0
        right = len(height)-1
        while left < right:
            maxArea = max(maxArea, min(height[right], height[left])*(right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


if __name__ == '__main__':
    height = [1,2,4,3]
    MA = MaxArea()
    print(MA.max_Area(height))