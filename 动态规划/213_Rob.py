#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/31 1:13 下午
# @Author : xiongtao
# @File : 213_Rob.py 
# @Title : 213. 打家劫舍 II

'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
'''

class Rob:
    def rob(self, nums):
        '''
        题解：动态规划
        1. 偷窃第0间房屋，那么第二间和最后一间就不能偷，因此最大的金额是[2:n]之间最大金额 + nums[0]
        2. 不偷窃第0间房屋，那么最大金额就是[1:n+1]之间最大的金额；

        至于怎么求区间内的最大金额，参考198题。
        '''
        n = len(nums)
        if n == 0:
            return 0
        if n <= 3:
            return max(nums)
        # [2:n]之间最大金额
        dp_0 = [0] * (n-3)
        dp_0[0] = nums[2]
        if n > 4:
            dp_0[1] = max(nums[3], nums[2])
        for i in range(2, n-3):
            dp_0[i] = max(dp_0[i-1], dp_0[i-2]+nums[i+2])
        # [1:n+1]
        dp_1 = [0] * (n-1)
        dp_1[0] = nums[1]
        dp_1[1] = max(nums[2], nums[1])
        for i in range(2, n-1):
            dp_1[i] = max(dp_1[i - 1], dp_1[i - 2] + nums[i+1])
        return max(dp_0[-1]+nums[0], dp_1[-1])

if __name__ == '__main__':
    R = Rob()
    nums = [200,3,140,20,10]
    print(R.rob(nums))


