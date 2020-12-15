#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/12/15 8:48 上午
# @Author : xiongtao
# @File : 042_Trap.py 
# @Title : 42. 接雨水

'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
'''

class Trap:
    def trap(self, height):
        # 维护一个栈，存的是递减数组
        deque = []
        index = 0
        cum_sum = 0
        while index < len(height):
            if index < len(height) - 1 and height[index + 1] < height[index]:
                deque.append(height[index])
                continue
            else:
                while index > 0 and height[index - 1] < height[index]:

                    curr_sum =

