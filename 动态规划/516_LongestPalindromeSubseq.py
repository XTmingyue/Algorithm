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
    题解：
    定义数组dp[i][j]:为字符串s中下标[i,j]最长的回文子序列。
    如何求dp[i][j]?
        1. 如果s[i] == s[j]，dp[i][j] = dp[i+1][j-1]+2。前提是j-1 >= i+1，即j - i >= 2;
        2. 如果s[i] != s[j]，dp[i][j] = max(dp[i+1][j], dp[i][j-1])。前提是j - i >= 1;

    证明：当s[i] == s[j]时，dp[i][j] 一定等于 dp[i+1][j-1]+2
    假设dp[i+1][j-1] = n:
        如果dp[i][j]最大回文子序列的左右边界是s[i]和s[j]，那么dp[i][j] = n + 2
        如果不是，那么要么左边界是s[i]但右边界不是s[j]，或者右边界是s[j]但左边界不是s[i]。
            不存在s[i] == s[j]时，左右边界不是s[i]和s[j]的情况，因为s[i] == s[j]本身就是回文子序列。
            假设左边界是s[i]但右边界不是s[j]，假设为s[k],k<j，那么dp[i][j-1] = b，且 b > n + 2。那么此时dp[i-1][j-1]
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




