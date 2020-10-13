#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/12 8:21 上午
# @Author : xiongtao
# @File : 123_MaxProfit.py 
# @Title : 123. 买卖股票的最佳时机 III

'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
'''

class MaxProfit:
    '''
    题解：动态规划
    定义数组dp[i][j][k]：表示下标为i时刻，是否持有股票（j=0表示不持有，j=1表示持有），卖出了k次（k=0、1、2）时的最大利润
    分为以下几种情形进行讨论；
    1. 不持有股票
        dp[i][0][0] = dp[i-1][0][0]
        dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][0] + prices[i]) // 要么i-1时刻就已经未持有且卖过一次，要么i-1时刻持有在i时刻卖出
        dp[i][0][2] = max(dp[i-1][0][2], dp[i-1][1][1] + prices[i])
    2. 持有股票
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - prices[i])
        dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][1] - prices[i])
        dp[i][1][2] //由于限制了最多只能完成两笔交易，因此不存在卖了2次后还持有股票的情况
    3. 初始化
        dp[0][0][:] = 0
        dp[0][1][:] = -prices[0]
    '''
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n)]
        for k in range(3):
            dp[0][0][k] = 0
            dp[0][1][k] = - prices[0]
        for i in range(n):
            dp[i][0][0] = dp[i - 1][0][0]
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][1][0] + prices[i])
            dp[i][0][2] = max(dp[i - 1][0][2], dp[i - 1][1][1] + prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i-1][0][0] - prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i-1][0][1] - prices[i])
            dp[i][1][2] = 0
        print(dp)
        return max(dp[n-1][0][1], dp[n-1][0][2])

if __name__ == '__main__':
    MP = MaxProfit()
    prices = [1,2,3,4,5]
    print(MP.maxProfit(prices))
