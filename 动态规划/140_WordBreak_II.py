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

'''
题解：递归
对于一个字符串s增加空格构成句子，如何拆分为子问题？
1. 定义函数wordBreak：返回字符串s可以构成的句子的集合；
2. 子问题拆分：
    a. 对于一个字符串s，可以拆分为s[0:k+1]以及单词s[k+1:]；
    b. 如果s[k+1:]在wordDict中 并且 s[0:k+1]可以拆分为wordDict中的单词组合，那么字符串s可能构成的句子的集合就是 s[0:k+1]构成的句子 加上 单词s[k+1:]；
    c. 如果s[k+1:]不在wordDict中，说明 s[k+1:] 不能单独构成单词，即s[0:k+1]与单词s[k+1:]不能新增空格；
3. 因为我们需要判断 s[0:k+1]是否可以拆分为wordDict中的单词组合，因此引出以下动态规划的方案，定义数组dp；
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
    # 返回s可以组成的所有组合， dp是所有为True的下标集合
    def wordBreakSub(self, s, wordDict, dp):
        # 当只剩一个元素时
        if s in wordDict:
            res = [s]
        else:
            res = []
        i = -1
        # 从右到左遍历dp数组
        while len(dp) + i >= 0:
            # 当s[k+1:] in wordDict中时，递归确定s[0:k+1]的所有组合
            if s[dp[i] + 1:] in wordDict:
                left_list = self.wordBreakSub(s[0: dp[i]+1], wordDict, dp[0:-1])
                for wordStr in left_list:
                    res.append(wordStr + ' ' + s[dp[i] + 1:])
            i -= 1
        return res
    # 计算dp数组
    def get_DP(self, s, wordDict):
        n = len(s)
        dp = [False] * n
        # 确定每个dp[i]的值
        for dp_i in range(0, n):
            if s[0:dp_i + 1] in wordDict:
                dp[dp_i] = True
            else:
                # s[j:dp_i + 1]至少要包含一个元素，因此j>0 and j<=dp_i
                for j in range(1, dp_i + 1):
                    if s[j: dp_i + 1] in wordDict:
                        dp[dp_i] = dp[dp_i] or dp[j - 1]
        return dp
    def wordBreak(self, s, wordDict):
        # 首先计算dp数组
        n = len(s)
        if n == 0:
            return []
        dp = self.get_DP(s, wordDict)
        dp_list = []
        for i in range(n):
            if dp[i]:
                dp_list.append(i)
        return self.wordBreakSub(s, wordDict, dp_list[0:-1])

if __name__ == '__main__':
    WB = WordBreak()
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(WB.wordBreak(s, wordDict))