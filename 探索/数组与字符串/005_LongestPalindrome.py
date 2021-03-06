#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/20 11:49 下午
# @Author : xiongtao
# @File : 005_LongestPalindrome.py 
# @Title : 最长回文子串

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

题解参考：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
'''
class LongestPalindrome():
    # 动态规划
    '''
    定义数组dp[i][j]表示字符串[i,j]是否是回文子串（左闭右闭），如果[i:j]是回文子串，那么[i+1:j-1]也是回文子串。
    那么dp[i][j] = (s[i]==s[j] & dp[i+1][j-1])，其中i+1<=j-1，即j - i >= 2
    当0< j - i < 2时，只需要判断s[i] == s[j]即可。
    时间复杂度：O(n^2)
    空间复杂度：O(n^2)
    '''
    def longestPalidrome(self, s):
        # 初始化数组d
        n = len(s)
        if n == 0:
            return ""
        d = [[False] * n for _ in range(n)]
        max_len = 0
        max_str = ""
        # 每次固定右边界j，遍历所有的 [i,j], 0<=i<=j 是否是回文序列，目的是为了保证d[i+1][j-1]已经计算过了
        for j in range(n):
            for i in range(j, -1, -1):
                d[i][j] = (s[i] == s[j])
                if j - i >= 2:
                    d[i][j] = d[i][j] and d[i + 1][j - 1]
                if d[i][j] and (j - i + 1) > max_len:
                    max_len = max(max_len, j - i + 1)
                    max_str = s[i:j + 1]
        return max_str

    # 中心扩散
    '''
    枚举每个中心点，从中心点往外扩散，看是否是回文子串。
    注意区分奇数子串中心是一个点，偶数子串中心是两个点
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    '''
    def findPalindrome(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    def longsetPalindrome_2(self, s):
        if len(s) <= 1:
            return s
        max_str = s[0]
        for i in range(0, len(s)-1):
            odd_find_str = self.findPalindrome(s, i, i)
            even_find_str = self.findPalindrome(s, i, i+1)
            if len(odd_find_str) > len(max_str):
                max_str = odd_find_str
            if len(even_find_str) > len(max_str):
                max_str = even_find_str
        return max_str

if __name__ == '__main__':
    LP = LongestPalindrome()
    s = "ccc"
    print(LP.longsetPalindrome_2(s))

