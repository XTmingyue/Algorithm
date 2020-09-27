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

'''
题解：
定义数组d[i][j]表示s[i: j+1]是否是回文子序列。
如果s[i: j+1]是回文子序列，那d[i+1][j-1] = True并且s[i] == s[j].
因此d[i][j] = (s[i] == s[j] and d[i+1][j-1])。
注意：0<=i+1<=j-1，即j-i >= 2。那么当0<j-i<2时，只需判断s[i]==s[j]即可。
'''

class Sloution:
    def longestPalindromeSubseq(self, s):
        # 初始化数组d
        n = len(s)
        if n == 0:
            return 0
        d = [[False] * n for _ in range(n)]
        # 只有一个元素时都是回文子串
        for i in range(n):
            d[i][i] = True
        max_len = 1




