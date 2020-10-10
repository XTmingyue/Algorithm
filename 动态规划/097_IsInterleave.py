#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/10 10:31 上午
# @Author : xiongtao
# @File : 097_IsInterleave.py 
# @Title : 97. 交错字符串

'''
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
示例 1：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
'''

class IsInterleave:
    # 递归 -- 超时
    # 返回s1 s2是否可以交错组成s3
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            if s2 == s3:
                return True
            else:
                return False
        if len(s2) == 0:
            if s1 == s3:
                return True
            else:
                return False
        if s3[-1] == s1[-1] and s3[-1] != s2[-1]:
            return self.isInterleave(s1[:-1], s2, s3[:-1])
        elif s3[-1] == s2[-1] and s3[-1] != s1[-1]:
            return self.isInterleave(s1, s2[:-1], s3[:-1])
        elif s3[-1] == s1[-1] and s3[-1] == s2[-1]:
            return self.isInterleave(s1[:-1], s2, s3[:-1]) or self.isInterleave(s1, s2[:-1], s3[:-1])
        else:
            return False
    # 动态规划
    # 定义数组dp[i][j]表示s1前i个元素与s2前j个元素是否可以交错组成s3前i+j个元素
    # 可知，s3的第i+j个元素要么等于s1第i个元素，要么等于s2第j个元素。
    # 由此推导出转移方程：
    # 1. 如果 s1[i-1] == s3[i+j-1]， 那么dp[i][j] = dp[i-1][j]
    # 2. 如果 s2[j-1] == s3[i+j-1]，那么dp[i][j] = dp[i][j-1]
    # 3. 如果 s1[i-1] == s3[i+j-1] 且 s2[j-1] == s3[i+j-1]， 那么dp[i][j] = dp[i-1][j] or dp[i][j-1]
    def isInterleave_2(self, s1, s2, s3):
        n, m, l = len(s1), len(s2), len(s3)
        if n + m != l:
            return False
        # 初始化数组dp
        dp = [[False] * (m + 1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(0, n+1):
            for j in range(0, m+1):
                # s3中第i+j元素下标
                p = i + j -1
                if i > 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[p]
                if j > 0:
                    dp[i][j] = dp[i][j] or (dp[i][j-1] and s2[j-1] == s3[p])
        return dp[n][m]

if __name__ == '__main__':
    class_IN = IsInterleave()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(class_IN.isInterleave_2(s1, s2, s3))
