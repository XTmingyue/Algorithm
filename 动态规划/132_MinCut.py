#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/14 8:32 上午
# @Author : xiongtao
# @File : 132_MinCut.py 
# @Title : 132. 分割回文串 II

'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回符合要求的最少分割次数。

示例:
输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
'''


import math
class MinCut:
    '''
    题解：递归 -- 超时
    定义函数minCut返回字符串s的最少分割次数
    1. 如果s就是回文串，返回0
    2. 如果s不是回文串，遍历s中每个字符作为分割点，那么以i为分割点的最少分割次数 = min(minCut(s[0:i]) + minCut(s[i+1:-1]) + 1)
    '''
    def isPalindromeStr(self, s):
        n = len(s) // 2
        for i in range(0, n):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

    def minCut(self, s):
        if self.isPalindromeStr(s):
            return 0
        min_cut = len(s)
        for i in range(1, len(s)):
            min_cut = min(min_cut, self.minCut(s[0:i]) + self.minCut(s[i:]) + 1)
        return min_cut

    '''
    题解：动态规划
    定义数组dp[i]：表示[0:i]子串最少的分割次数
    求转移方程：
    1. 如果[0:i]就是回文串，那么就不需要分割，dp[i] = 0
    2. 如果[0:i]不是回文串，我们遍历[0:i]之间的数字k进行分割，当[k:i]是回文串时dp[i] = min(dp[k] + 1)
    由于一直需要判断[k:i]是否是回文串，因此考虑申请一个二维数组nums[i][j]用于存储[i:j]是否是回文串
    '''
    # 判断任意i～j之间是否是回文串
    def palindromeSub(self, nums, s):
        '''
        采用动态规划的方式计算任意子串是否是回文串
        num[i][j]:表示i～j是否是回文串
        当s[i] == s[j]时，nums[i][j] = nums[i+1][j-1]
        当s[i] != s[j]时，nums[i][j] = 0
        '''
        n = len(s)
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                nums[i][j] = (s[i] == s[j])
                if i + 1 <= j - 1 and s[i] == s[j]:
                    nums[i][j] = nums[i][j] and nums[i+1][j-1]

    def minCut_2(self, s):
        n = len(s)
        dp = [math.inf] * n
        dp[0] = 0
        nums = [[False] * n for _ in range(n)]
        # 任意单个字符都是回文串
        for i in range(n):
            nums[i][i] = True
        self.palindromeSub(nums, s)
        for i in range(1, n):
            # 如果本身就是回文串，就不需要分割
            if nums[0][i]:
                dp[i] = 0
            else:
                for k in range(0, i):
                    if nums[k + 1][i]:
                        dp[i] = min(dp[i], dp[k] + 1)
        return dp[-1]


if __name__ == '__main__':
    MC = MinCut()
    s = "aab"
    print(MC.minCut(s))