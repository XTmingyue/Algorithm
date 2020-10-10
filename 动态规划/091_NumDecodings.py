#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/9 10:32 上午
# @Author : xiongtao
# @File : 091_NumDecodings.py 
# @Title : 91. 解码方法

'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:
输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2:
输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
'''

class NumDecodings:
    '''
    题解：动态规划
    我们可以类比上楼梯的问题，每次可以解码一个数字，也可以解码两个数字。
    但是需要注意的是:
        1. 两个数字的大小不能超过26
        2. 数字0不能进行单独解码，且只能作为两位数中的后一位，如10就是合法的，01就是不合法的
    定义数组dp[i]：表示[0, i]个数字的解码方法总数。给出转移方程：
    分成以下两种情况：
    1. s[i-1:i+1]可以合并解码，即 s[i-1:i+1] in [10, 26]
        a. 如果 s[i-1:i+1] == 10/20，那么s[i-1:i+1]只能合并解码，即dp[i] = dp[i-2]
        b. 如果 s[i-1:i+1] != 10/20，那么s[i-1:i+1]既能合并解码也可以拆分解码，即dp[i] = dp[i-2] + dp[i-1]
    2. s[i-1:i+1]不可以合并解码，即 s[i-1:i+1] not in [10, 26]
        a. 如果 s[i] == 0，那么无法解码，即dp[i] = 0
        b. 如果 s[i] != 0，那么s[i]只能单独进行解码，即dp[i] = dp[i-1]
    '''
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        # 初始化数组
        dp = [0] * len(s)
        dp[0] = 1
        if s[0:2] >= '10' and s[0:2] <= '26':
            if s[0:2] == '10' or s[0:2] == '20':
                dp[1] = 1
            else:
                dp[1] = 2
        else:
            if s[1] == '0':
                dp[1] = 0
            else:
                dp[1] = 1
        for i in range(2, len(s)):
            if s[i-1:i+1] >= '10' and s[i-1:i+1] <= '26':
                if s[i-1:i+1] == '10' or s[i-1:i+1] == '20':
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-2] + dp[i-1]
            else:
                if s[i] == '0':
                    dp[i] = 0
                else:
                    dp[i] = dp[i-1]
        return dp[-1]

if __name__ == '__main__':
    class_ND = NumDecodings()
    s = "301"
    print(class_ND.numDecodings(s))