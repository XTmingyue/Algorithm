#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/9 11:51 下午
# @Author : xiongtao
# @File : 053_MaxSubArray.py 
# @Title : 53. 最大子序和

'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

class MaxSubArray:
    # 动态规划：
    # 定义f(i):以nums[i]为最后一个元素的最大和连续子数组之和
    # 那么maxSubArray返回的就是max f(i)
    # f(i)与f(i-1)的关系：f(i) = max(nums[i], f(i-1)+nums[i])
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return None
        res = nums[0]
        max_sub = nums[0]
        for i in range(1, len(nums)):
            res = (max(nums[i], res + nums[i]))
            if res > max_sub:
                max_sub = res
        return max_sub

if __name__ == '__main__':
    class_MSA = MaxSubArray()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(class_MSA.maxSubArray(nums))
