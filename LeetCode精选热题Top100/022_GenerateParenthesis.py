#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/11/28 9:57 下午
# @Author : xiongtao
# @File : 022_GenerateParenthesis.py 
# @Title : 22. 括号生成

'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
'''

class Solution:
    '''
    题解：动态规划
    已知1～n-1个括号组成的有效括号的所有组合 nums
    要求n个括号组成的有效括号的所有组合，那么对于第n个括号如何与剩下的n-1个括号进行组合？
    任何一个括号序列都一定是由 ( 开头，并且第一个 ( 一定有一个唯一与之对应的 )。
    这样一来，每一个括号序列可以用 (p)q 来表示，其中 p 与 q 分别是一个合法的括号序列（可以为空）
    "(" + p个括号 + ")" + q个括号
    其中，p + q = n-1
    '''
    def generateParenthesis(self, n):
        if n == 0:
            return []
        # 定义二维数组存储任意i个括号组成的有效括号
        dp = []
        # 0个括号表示组合为空
        dp.append([None])
        # 1个括号
        dp.append(["()"])
        # 遍历所有可能
        for i in range(2, n+1):
            p = 0
            q = i - 1
            res = []
            while p <= i - 1:
                for val_1 in dp[p]:
                    for val_2 in dp[q]:
                        str_1 = val_1
                        str_2 = val_2
                        if val_1 == None:
                            str_1 = ""
                        if val_2 == None:
                            str_2 = ""
                        res.append("(" + str_1 + ")" + str_2)
                p += 1
                q -= 1
            dp.append(res)
        return dp[-1]

if __name__ == '__main__':
    class_S = Solution()
    n = 3
    print(class_S.generateParenthesis(n))



