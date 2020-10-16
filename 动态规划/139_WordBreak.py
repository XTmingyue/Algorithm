#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/15 9:49 下午
# @Author : xiongtao
# @File : 139_WordBreak.py 
# @Title : 139. 单词拆分

'''
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
'''

'''
题解：动态规划
定义数组dp[i]：表示0～i的子串是否可以被拆分为一个或多个在字典中出现的单词
转移方程：
1. 若[0:i]本身就在字典中，dp[i] = 1
2. 若[0:i]本身不在字典中，遍历0～i中的元素k进行分割，如果[k:i]在字典中，那么dp[i] = dp[i] or dp[k]
'''

class WordBreak:
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * n
        # 遍历每一个[0:i]的子串
        for i in range(1, n + 1):
            if s[0:i] in wordDict:
                dp[i - 1] = True
            else:
                # 遍历[0:i]之间的值，由于[k:i]不能为NULL，因此k只能取1～i-1
                for k in range(1, i):
                    if s[k:i] in wordDict:
                        dp[i - 1] = dp[i - 1] or dp[k - 1]
        return dp[-1]

if __name__ == '__main__':
    WB = WordBreak()
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(WB.wordBreak(s, wordDict))