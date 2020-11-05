#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/11/5 8:23 上午
# @Author : xiongtao
# @File : 003_LengthOfLongestSubstring.py 
# @Title : 3. 无重复字符的最长子串

'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

class Solution:
    def lengthOfLongestSubstring(self, s:str):
        # 定义数组dp[i]表示以i为结尾的最长子串的长度
        n = len(s)
        if n == 0:
            return 0
        dp = [1]*n
        max_len = 1
        for i in range(1, n):
            last_len = dp[i-1]
            if s[i] not in s[i-last_len:i]:
                dp[i] = last_len + 1
            else:
                cum = 1
                for j in range(i-1, -1, -1):
                    if s[i] != s[j]:
                        cum += 1
                    else:
                        break
                dp[i] = cum
            max_len = max(max_len, dp[i])
        return max_len

if __name__ == '__main__':
    S = Solution()
    s = "dvdf"
    print(S.lengthOfLongestSubstring(s))
