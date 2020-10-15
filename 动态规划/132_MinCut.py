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

class MinCut:
    '''
    题解：动态规划
    定义数组dp[i]：表示[0:i]子串最少的分割次数
    求转移方程：
    我们遍历[0:i]之间的数字k进行分割，当[k:i]是回文串时dp[i] = min(dp[k] + 1)
    同时由于一直需要判断[k:i]是否是回文串，因此考虑申请一个二维数组nums[i][j]用于存储[i:j]是否是回文串
    '''
    def palindromeSub(self, nums, s):

    def minCut(self, s):
        n = len(s)
        dp = [0] * n
        nums = [[0] * n for _ in range(n)]



