#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/31 1:52 下午
# @Author : xiongtao
# @File : 221_MaximalSquare.py 
# @Title : 221. 最大正方形

'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:
输入:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
'''



class MaximalSquare:
    '''
    题解：
    定义数组dp[i][j]：表示第i行第j个元素上有多少个1
    遍历数组dp的每一行，计算可以构成的最大正方形。

    对于第i行，如何求解dp[i][:]构成的最大正方形。
    要计算第i行中以j为右边界的最大正方形，只需要找到第i行中各个波峰进行计算即可。
    '''
    def maximalSquare(self, matrix):
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        # 初始化数组
        for j in range(m):
            cum_num = 0
            for i in range(n):
                if matrix[i][j] == "0":
                    cum_num = 0
                else:
                    cum_num += 1
                dp[i][j] = cum_num
        # 计算最大正方形
        max_Square = 0
        for i in range(n):
            for j in range(1, m):
                # 判断是否峰值
                if dp[i][j] < dp[i][j-1]:
                    min_len = dp[i][j-1]
                    max_Square = max(1, max_Square)
                    for k in range(j-2, -1, -1):
                        min_len = min(min_len, dp[i][k])
                        if min_len >= (j-1-k+1):
                            max_Square = max(max_Square, (j-k)*(j-k))
            # 最后一个不管是不是峰值都进行计算
            min_len = dp[i][m-1]
            if min_len > 0:
                max_Square = max(1, max_Square)
            for k in range(m-2, -1, -1):
                min_len = min(min_len, dp[i][k])
                if min_len >= (m - 1 - k + 1):
                    max_Square = max(max_Square, (m - k) * (m - k))
        return max_Square

    '''
    题解：动态规划
    定义数组dp[i][j]：表示以[i][j]为右下角的正方形的最大边长
    转移方程：dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    证明：https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/solution/tong-ji-quan-wei-1-de-zheng-fang-xing-zi-ju-zhen-2/
    '''
    def maximalSquare_2(self, matrix):
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        max_len = 0
        # 初始化边界
        for i in range(n):
            if matrix[i][0] == "0":
                dp[i][0] = 0
            else:
                dp[i][0] = 1
                max_len = 1
        for j in range(m):
            if matrix[0][j] == "0":
                dp[0][j] = 0
            else:
                dp[0][j] = 1
                max_len = 1
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = 0
                max_len = max(max_len, dp[i][j])
        return max_len*max_len


if __name__ == '__main__':
    MS = MaximalSquare()
    matrix = [["1","0"]]
    print(MS.maximalSquare_2(matrix))