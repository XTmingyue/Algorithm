#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/19 8:38 下午
# @Author : xiongtao
# @File : 062_UniquePaths.py 
# @Title : 62. 不同路径

'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
'''

class UniquePaths:
    def uniquePaths(self, m, n):
        p = [[0]*n for _ in range(m)]
        p[0][0] = 1
        for i in range(m):
            p[i][0] = 1
        for j in range(n):
            p[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                p[i][j] = p[i-1][j] + p[i][j-1]
        return p[m-1][n-1]

if __name__ == '__main__':
    class_UP = UniquePaths()
    m = 3
    n = 2
    print(class_UP.uniquePaths(m, n))


