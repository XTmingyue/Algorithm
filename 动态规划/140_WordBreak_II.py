#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/16 8:39 上午
# @Author : xiongtao
# @File : 140_WordBreak_II.py 
# @Title : 140. 单词拆分 II

'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。
返回所有这些可能的句子。
说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]

示例 2：
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
'''

class WordBreak:
    '''
    题解：动态规划
    1. 沿用139题中的转移数组dp[i]：表示s[0:i+1]是否可以被拆分为wordDict数组中的元素组合
    2. dp[len(s)-1] == False时，说明s不能被拆分为wordDict中的元素组合，那么直接返回 []
    3. dp[len(s)-1] == True时，我们采用递归的方式求解所有可能的组合：
        a. 从右到左遍历dp数组中的元素k，当s[k+1:] in wordDict中时，递归确定s[0:k+1]的所有组合；
        b. 注意可能存在多个k满足 s[k+1:] in wordDict中，对于每一种都要递归的确定s[0:k+1]的所有组合；
    '''
    def wordBreak(self, s, wordDict):
        # 首先计算dp数组
        n = len(s)
        if n == 0:
            return []
        dp = [False] * n
        for i in range(0, n):
            if s[0:i+1] in wordDict:
                dp[i] = True
            else:
                for j in range(1, i):
                    if s[j:i+1] in wordDict:
                        dp[i] = dp[i] or dp[j-1]

        return dp[-1]

if __name__ == '__main__':
    WB = WordBreak()
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(WB.wordBreak(s, wordDict))