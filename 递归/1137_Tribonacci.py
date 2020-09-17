#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/6 10:50 下午
# @Author : xiongtao
# @File : 1137_Tribonacci.py 
# @Title : 1137. 第 N 个泰波那契数

'''
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        save_nums = [0, 1, 1]
        for i in range(3, n+1):
            res = save_nums[0] + save_nums[1] + save_nums[2]
            save_nums[0], save_nums[1], save_nums[2] = save_nums[1], save_nums[2], res
        return save_nums[2]



