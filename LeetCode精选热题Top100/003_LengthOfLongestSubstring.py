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
    '''
    题解：滑动窗口解法
    假设以i开始的最长子串为[i:j]，那么我们要计算以i+1开始的最长子串。
    首先可以知道[i+1:j]也一定不含重复字符的子串，我们将j往后移，并判断j元素是否在[i+1:j]内即可。
    '''
    def lengthOfLongestSubstring_2(self, s: str):
        if s == '':
            return 0
        curr_set = set(s[0])
        max_len = 1
        j = 1
        for i in range(0, len(s)):
            curr_len = j - i
            while j < len(s):
                if s[j] not in curr_set:
                    curr_len += 1
                    curr_set.add(s[j])
                    j += 1
                    max_len = max(max_len, curr_len)
                else:
                    max_len = max(max_len, curr_len)
                    break
            curr_set.remove(s[i])
        return max_len

if __name__ == '__main__':
    S = Solution()
    s = "dvdf"
    print(S.lengthOfLongestSubstring_2(s))
