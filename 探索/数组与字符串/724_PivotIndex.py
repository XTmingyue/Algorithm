#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/17 11:44 下午
# @Author : xiongtao
# @File : 724_PivotIndex.py

'''
题目：给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。

我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

输入：
nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
索引 3 (nums[3] = 6) 的左侧数之和 (1 + 7 + 3 = 11)，与右侧数之和 (5 + 6 = 11) 相等。
同时, 3 也是第一个符合要求的中心索引。
'''

class PivotIndex():
    def pivotIndex(self, nums):
        if len(nums) == 0:
            return -1
        sum = 0
        for val in nums:
            sum += val
        res_index = -1
        right_sum = 0
        for i in range(0, len(nums)):
            if (sum-nums[i])/2 == right_sum:
                return i
            else:
                right_sum += nums[i]
        return res_index

if __name__ == '__main__':
    PI = PivotIndex()
    nums = [-1,-1,-1,0,1,1]
    print(PI.pivotIndex(nums))