#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/19 10:09 下午
# @Author : xiongtao
# @File : 070_ClimbStairs.py 
# @Title : 70. 爬楼梯

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
'''

class ClimbStairs:
    def climbStairs(self, n):
        if n <= 1:
            return n
        # 初始化数组p[i]表示爬到i台阶的方法数
        p = [0]*n
        p[0] = 1
        p[1] = 2
        for i in range(2, n):
            p[i] = p[i-1] + p[i-2]
        return p[n-1]

if __name__ == '__main__':
    class_CS = ClimbStairs()
    n = 3
    print(class_CS.climbStairs(n))
