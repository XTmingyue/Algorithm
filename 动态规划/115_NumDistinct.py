#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/10 5:05 下午
# @Author : xiongtao
# @File : 115_NumDistinct.py 
# @Title : 115. 不同的子序列

'''
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

输入：S = "rabbbit", T = "rabbit"
输出：3
解释：

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
'''

'''
题解：动态规划
定义数组dp[i][j]:s前i个字符组成的子序列中t前j个字符出现的次数。
推导转移方程：
1. 当s[i-1] == t[j-1]时，我们可以将s中等于t前j个字符的子序列分为两类：
    a. 子序列最后一个是s[i-1]，此时次数 = dp[i-1][j-1]
    b. 子序列最后一个不是s[i-1]，此时次数 = dp[i-1][j]
    因此，有dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
2. 当s[i-1] != t[j-1]时，此时dp[i][j] = dp[i-1][j]

初始化数组dp：
1. 当字符串t是空字符串时，s的子序列中t出现的次数为1。即dp[i][0] = 1
2. 只有当i >= j时，dp[i][j]才有计算的必要
'''

class Solution:
    def numDistinct(self, s, t):
        if len(s) < len(t):
            return 0
        n, m = len(s), len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(0, n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i >= j:
                    if s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
        return dp[n][m]

if __name__ == '__main__':
    class_S = Solution()
    S = "babgbag"
    T = "bag"
    print(class_S.numDistinct(S, T))