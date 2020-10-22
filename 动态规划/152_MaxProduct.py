#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/21 12:39 下午
# @Author : xiongtao
# @File : 152_MaxProduct.py 
# @Title : 152. 乘积最大子数组

'''
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''

class MaxProduct:
    '''
    题解：动态规划 -- 超时
    定义数组dp[i]：表示截止下标为i时，0～i中最大的连续子数组的乘积
    1. 最大连续子数组以i为最后一个元素时，往前遍历
    2. 最大连续子数组不以i为最后一个元素时，dp[i] = dp[i-1]
    '''
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            product = nums[i]
            dp[i] = product
            for j in range(i - 1, -1, -1):
                product *= nums[j]
                dp[i] = max(product, dp[i])
            dp[i] = max(dp[i-1], dp[i])
        return dp[-1]
    '''
    题解：动态规划
    注意因为会有负值，因此需要判断第i个元素是正数还是负数，正数时就乘上i-1时的最大值，负数时就乘上i-1时的最小时。
    
    定义数组dp_max[i]：表示以下标i为最后一个元素的最大的连续子数组的乘积
    定义数组dp_min[i]：表示以下标i为最后一个元素的最小的连续子数组的乘积
    1. 如果nums[i] >= 0
        dp_max[i] = max(dp_max[i-1]*nums[i], nums[i])
        dp_min[i] = min(dp_min[i-1]*nums[i], nums[i])
    2. 如果nums[i] < 0
        dp_max[i] = max(dp_min[i-1]*nums[i], nums[i])
        dp_min[i] = min(dp_max[i-1]*nums[i], nums[i])
        
    '''
    def maxProduct_2(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp_max = [0] * n
        dp_max[0] = nums[0]

        dp_min = [0] * n
        dp_min[0] = nums[0]

        res = dp_max[0]
        for i in range(1, n):
            if nums[i] >= 0:
                dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i])
                dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i])
            else:
                dp_max[i] = max(dp_min[i - 1] * nums[i], nums[i])
                dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i])
            res = max(res, dp_max[i])
        return res

if __name__ == '__main__':
    MP = MaxProduct()
    nums = [2,3,-2,4]
    print(MP.maxProduct_2(nums))
