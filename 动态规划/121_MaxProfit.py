#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/11 10:28 上午
# @Author : xiongtao
# @File : 121_MaxProfit.py 
# @Title : 121. 买卖股票的最佳时机

'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

'''
题解：动态规划
定义数组dp[i]：表示第i-1天时的最大利润
求解转移方程，分为以下两种情况：
1. prices[i] 卖出时，最大利润为[0:i]之间的最小值min_num买进，此时dp[i] = prices[i] - min_num
2. prices[i] 不卖，dp[i] = dp[i-1]
因此，dp[i] = max(prices[i] - min_num, dp[i-1])
'''
class MaxProfit:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        min_num = prices[0]
        dp = [0] * n
        for i in range(1, n):
            min_num = min(min_num, prices[i-1])
            dp[i] = max(prices[i] - min_num, dp[i-1])
        return dp[-1]

if __name__ == '__main__':
    MP = MaxProfit()
    prices = [7,6,4,3,1]
    print(MP.maxProfit(prices))
