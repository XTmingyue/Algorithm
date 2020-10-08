#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/27 8:55 上午
# @Author : xiongtao
# @File : 516_LongestPalindromeSubseq.py 
# @Title : 516. 最长回文子序列

'''
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

输入:"bbbab"
输出:4
一个可能的最长回文子序列为 "bbbb"。
'''


class Sloution:
    '''
    题解：动态规划
    定义数组dp[i][j]:为字符串s中下标[i,j]最长的回文子序列。
    如何求dp[i][j]?
        1. 如果s[i] == s[j]，dp[i][j] = dp[i+1][j-1]+2。前提是j-1 >= i+1，即j - i >= 2;
        2. 如果s[i] != s[j]，dp[i][j] = max(dp[i+1][j], dp[i][j-1])。前提是j - i >= 1;

    证明：当s[i] == s[j]时，dp[i][j] 一定等于 dp[i+1][j-1]+2
    1. 假设dp[i+1][j-1] = n，那么一定有dp[i][j] >= n + 2
    2. 如果 dp[i][j] > n + 2，那么最长回文子序列要么左边界为s[i]，要么右边界为s[j]，且不能同时满足;
        - 因为如果左边界为s[i]且右边界为s[j]，那么dp[i][j] = n + 2
        - 假设最长回文子序列左边界为s[i]，那么dp[i][j] = b > n + 2
        - 我们去掉s[i]以及s[i, j-1]中与s[i]匹配的回文字符，剩下的字符能够从最长的回文子序列为dp[i+1][j-1] = b - 2
        - 而我们前面假设了dp[i+1][j-1] = n, 因此b - 2 = n，这与b > n + 2矛盾了
        - 因此dp[i][j] = n + 2
    '''
    def longestPalindromeSubseq(self, s):
        n = len(s)
        if n <= 1:
            return n
        # 初始化数组
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n-1]

if __name__ == '__main__':
    class_S = Sloution()
    s = "bbb"
    print(class_S.longestPalindromeSubseq(s))




