#!/usr/bin python
# -*- coding: utf-8 -*- 

# @Time : 2020/10/26 11:22 AM 
# @Author : xiongtao
# @File : 188_MaxProfit.py
# @Title : 188. 买卖股票的最佳时机 IV

'''
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2：
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

'''

'''
题解：动态规划
定义数组dp[i][j][k]:表示下标为i时刻，是否持有股票（j=0/1），已经交易k笔时刻的最大利润；
1. 当前未持有股票时，即j=0时，求dp[i][0][k]的转移方程：
    当 k = 0 时，dp[i][0][k] = dp[i-1][0][k]
    当 k > 0 时，要么i-1时刻卖出了股票，要么i-1时刻就是未持有状态：dp[i][0][k] = max(dp[i-1][0][k], dp[i-1][1][k-1] + prices[i])

2. 当前是持有股票时，即j=1时，求dp[i][1][k]的转移方程：
    当 k <= K-1 时，dp[i][1][k] = max(dp[i-1][1][k], dp[i-1][0][k] - prices[i])
    当 k = K 时，因为已经达到最大的交易次数了，因此dp[i][1][K]不存在
3. 初始化
    dp[0][1][:] = -prices[0]
    dp[0][0][:] = 0
'''

class MaxProfit:
    def maxProfit(self, k, prices):
        if len(prices) == 0:
            return 0
        n = len(prices)
        dp = [[[0] * (k+1) for _ in range(2)] for _ in range(n)]
        for m in range(k+1):
            dp[0][1][m] = - prices[0]
            dp[0][0][m] = 0

        for i in range(1, n):
            for m in range(0, k+1):
                if m == 0:
                    dp[i][0][m] = dp[i - 1][0][m]
                else:
                    dp[i][0][m] = max(dp[i - 1][0][m], dp[i - 1][1][m - 1] + prices[i])

                if m < k:
                    dp[i][1][m] = max(dp[i-1][1][m], dp[i-1][0][m] - prices[i])
        max_res = 0
        for m in range(k+1):
            max_res = max(max_res, dp[n-1][0][m])
        return max_res

if __name__ == '__main__':
    MP = MaxProfit()
    k = 2
    prices = [2, 4, 1]
    print(MP.maxProfit(k, prices))






