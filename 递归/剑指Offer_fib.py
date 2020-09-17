#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/6 11:44 下午
# @Author : xiongtao
# @File : 剑指Offer_fib.py 
# @Title :剑指 Offer 10- I. 斐波那契数列

'''
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
'''

class Solution:
    # 返回fib(n)
    def fibonacci(self, n, nums):
        res = nums[n-1] + nums[n-2]
        nums.append(res)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [0, 1]
        for i in range(2, n+1):
            self.fibonacci(i, nums)
        return nums[-1]%1000000007

if __name__ == '__main__':
    class_slu = Solution()
    print(class_slu.fib(5))