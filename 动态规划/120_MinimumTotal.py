#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/11 9:32 上午
# @Author : xiongtao
# @File : 120_MinimumTotal.py 
# @Title : 120. 三角形最小路径和

'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
'''

import math

class MinTotal:
    '''
    题解：动态规划
    定义数组dp[i][j]：表示从[0, 0]~[i, j]的最小路径和
    由于dp[i][j]只能由dp[i-1][j-1]以及dp[i-1][j]移动而来。
    因此，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    '''
    def minimumTotal(self, triangle):
        if len(triangle) == 0:
            return 0
        n, m = len(triangle), len(triangle[len(triangle) - 1])
        dp = [[math.inf] * m for _ in range(n)]
        # 初始化数组
        for j in range(len(triangle[0])):
            dp[0][j] = triangle[0][j]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]

        for i in range(1, n):
            for j in range(1, len(triangle[i])):
                # 空白的元素填充的无穷大，因此可直接计算最小值
                dp[i][j] = min(dp[i - 1][j - 1], dp[i-1][j]) + triangle[i][j]
        # 计算最小值
        min_num = None
        for j in range(m):
            min_num = dp[n-1][j] if min_num == None else min(min_num, dp[n-1][j])
        return min_num

    '''
    动态规划--优化空间复杂度
    计算第i行的最小路径时只用到了dp数组第i-1行的数据以及triangle数组第i行的数据。
    因此，我们可以只申请一维的dp数组，且计算dp[j]要用到dp[j-1]、dp[j]以及triangle[i][j]，因此我们要从右到左进行遍历。
    dp[j]:表示当前行下标为j的元素最小路径。
    dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
    '''
    def minimumTotal_2(self, triangle):
        if len(triangle) == 0:
            return 0
        n = len(triangle[len(triangle) - 1])
        dp = [math.inf] * n
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(i, -1, -1):
                if j > 0:
                    dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]
                else:
                    dp[j] = dp[j] + triangle[i][j]
        # 计算最小值
        min_num = None
        for j in range(n):
            min_num = dp[j] if min_num == None else min(min_num, dp[j])
        return min_num


if __name__ == '__main__':
    minTotal = MinTotal()
    triangle = [[-1],[-2,-3]]
    print(minTotal.minimumTotal_2(triangle))

