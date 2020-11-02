#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/31 12:47 下午
# @Author : xiongtao
# @File : 198_Rob.py 
# @Title : 198. 打家劫舍

'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
'''

class Rob:
    def rob(self, nums):
        '''
        题解：动态规划
        dp[i]表示：截止下标为i的房屋，小偷可以偷窃的最高金额。存在以下两种情况：
        1. i房屋偷：dp[i] = dp[i-2] + nums[i]
        2. i房屋不偷：dp[i] = dp[i-1]
        因此，dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        '''
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        # 初始化
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
if __name__ == '__main__':
    R = Rob()
    nums = [1,2,3,1]
    print(R.rob(nums))

