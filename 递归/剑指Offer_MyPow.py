#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/8 12:24 上午
# @Author : xiongtao
# @File : 剑指Offer_MyPow.py 
# @Title : 剑指 Offer 16. 数值的整数次方

'''
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。
输入: 2.00000, 10
输出: 1024.00000
'''

# 二分法
# n为偶数时：x^n = (x^(n/2))^2
# n为奇数时：x^n = x*(x^((n-1)/2))^2
class MyPow:
    def abs_pow(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            res = self.abs_pow(x, n/2)
            return res * res
        else:
            res = self.abs_pow(x, (n-1)/2)
            return x * res * res
    # 返回x^n
    def myPow(self, x, n):
        if n < 0:
            return 1/self.abs_pow(x, abs(n))
        else:
            return self.abs_pow(x, abs(n))

