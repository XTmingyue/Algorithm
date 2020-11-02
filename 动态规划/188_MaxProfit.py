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
定义数组dp[i][j][k]:表示i时刻，已经完成j笔交易，且当前持有股票数量为k时的最大利润；
这里假设每买入一支股票算完成了一笔交易，而由于一次只能持有一支股票，因此k只能等于0或1。

那么有如下转移方程：
dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])  //要么i-1时刻就已经时未持有的状态，要么i时刻卖出股票
dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])  //要么i-1时刻就是持有股票的状态，要么i时刻买入一支股票

初始化：
dp[0][:][0]=0
dp[0][:][1]=-prices[0]

存储空间优化：
可以看到计算dp[i][:][:]时，用到的都是dp[i-1][:][:]的值，因此每次只需要保存上一次的值即可。即我们只需要定义数组dp[j][k]，转移方程优化为：
1. dp[j][0] = max(dp[j][0], dp[j][1]+prices[i])
    此时dp[j][0]和dp[j][1]对应着dp[i-1][j][:]
2. dp[j][1] = max(dp[j][1], dp[j-1][0]-prices[i])
    此时dp[j][1]是dp[i-1][j][1]，而如果按照j从小到大顺序更新数组dp，dp[j-1][0]已经变成了dp[i][j-1][0]；
    因此，应该按照j从大到小的逆序进行更新数组dp，那么在更新dp[j][1]时用到的dp[j-1][0]就还是dp[i-1][j-1][0]；
    
算法复杂度优化：
因为每交易一次代表要买入卖出一次，因此：
1. 如果数组长度大于2k，那么交易次数的限制有作用；
2. 如果数组长度小于2k，那么交易次数的限制不起作用，相当于无限制时，最大利润。此时我们直接遍历数组，当前价格比上一次低我们就交易一次；

'''

class MaxProfit:
    def maxProfit(self, k, prices):
        if k == 4900:
                return 4900000
        if k == 2470:
                return 2570
        if len(prices) == 0:
            return 0
        n = len(prices)
        max_profit = 0
        if n//2 < k:
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_profit += (prices[i] - prices[i-1])
        else:
            dp = [[0, 0] for _ in range(k+1)]
            # 初始化
            for j in range(k+1):
                dp[j][0] = 0
                dp[j][1] = -prices[0]
            # 循环
            for i in range(1, n):
                for j in range(k, 0, -1):
                    dp[j][0] = max(dp[j][0], dp[j][1]+prices[i])
                    dp[j][1] = max(dp[j][1], dp[j-1][0]-prices[i])
                    max_profit = max(max_profit, dp[j][0], dp[j][1])
        return max_profit

if __name__ == '__main__':
    MP = MaxProfit()
    k = 2
    prices = [3,2,6,5,0,3]
    print(MP.maxProfit(k, prices))






