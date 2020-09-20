#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/19 10:01 下午
# @Author : xiongtao
# @File : 064_MinPathSum.py 
# @Title : 64. 最小路径和

'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''

'''
题解：采用动态规划进行求解。定义数组p[i][j]表示从[0,0]到[i,j]的路径最小和。
p[i][j] = min(p[i][j-1], p[i-1][j]) + grid[i][j]
'''
class MinPathSum:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        # 初始化数组
        p = [[0] * n for _ in range(m)]
        p[0][0] = grid[0][0]
        for i in range(1, m):
            p[i][0] = p[i-1][0] + grid[i][0]
        for j in range(1, n):
            p[0][j] = p[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                p[i][j] = min(p[i][j - 1], p[i - 1][j]) + grid[i][j]
        return p[m-1][n-1]

if __name__ == '__main__':
    class_MPS = MinPathSum()
    grid = [[1,3,1], [1,5,1], [4,2,1]]
    print(class_MPS.minPathSum(grid))