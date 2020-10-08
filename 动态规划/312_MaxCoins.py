#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/29 9:14 下午
# @Author : xiongtao
# @File : 312_MaxCoins.py 
# @Title : 312. 戳气球

'''
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 
这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。

说明:
- 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''

'''
题解：动态规划
定义数组dp[i][j]为只戳破(i, j)之间的气球，[i, j]之间能获得硬币的最大数量。注意这里i和j是不能戳破的。
dp[i][j]的推导式：
我们遍历(i, j)中的数k，计算当k作为[i, j]中最后一个戳破的气球时，获得硬币的最大数量。
dp[i][j] = max(dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])

为便于计算同时避免越界，我们在首尾分别新增数字为1的气球。这样我们只需要求dp[0][len(nums)-1]即是最终结果。
'''

class MaxCoins:
    def maxCoins(self, nums):
        if len(nums) == 0:
            return 0
        nums.insert(0, 1)
        nums.insert(len(nums), 1)
        # 初始化数组
        dp = [[0] * len(nums) for _ in range(len(nums))]
        # 画出dp数组的计算过程可知，要计算dp[i][j]，就要先计算dp[i][k]和dp[k][j]
        # 即计算过程中dp[i][k]和dp[k][j]要已知，那么我们每次固定j将j左侧的值都计算出来
        for j in range(2, len(nums)):
            for i in range(j - 1, -1, -1):
                max_coins = 0
                for k in range(i + 1, j):
                    max_coins = max(max_coins, dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k])
                dp[i][j] = max_coins
        return dp[0][len(nums) - 1]

if __name__ == '__main__':
    class_MC = MaxCoins()
    nums = [3,1,5,8]
    print(class_MC.maxCoins(nums))