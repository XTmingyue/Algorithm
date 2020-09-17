#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/8 12:36 上午
# @Author : xiongtao
# @File : 面试题 08.05_Multiply.py 
# @Title : 面试题 08.05. 递归乘法

'''
递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

输入：A = 1, B = 10
 输出：10
'''

class Multiply:
    def abs_multiply(self, A, B):
        if A == 1:
            return B
        return self.abs_multiply(A - 1, B) + B
    def multiply(self, A, B):
        # 保证A是最小的数
        a = abs(A)
        b = abs(B)
        if a > b:
            a, b = b, a
        res = self.abs_multiply(a, b)
        if (A > 0 and B > 0) or (A < 0 and B < 0):
            return res
        else:
            return -1 * res
