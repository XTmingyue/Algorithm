#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/19 9:49 下午
# @Author : xiongtao
# @File : 063_UniquePathsWithObstacles.py
# @Title : 63. 不同路径 II

'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
'''

'''
题解：同样定义数组p[i][j]为从[0,0]到[i,j]的路径条数。
由于存在障碍，需要进行判断。
1. obstacleGrid[i-1][j]==1，p[i][j] = p[i][j-1]
2. obstacleGrid[i][j-1]==1, p[i][j] = p[i-1][j]
3. obstacleGrid[i-1][j]==1 and obstacleGrid[i][j-1]==1, p[i][j] = 0
'''
class UniquePaths:
    def uniquePaths(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        p = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        p[0][0] = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            p[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            p[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                if obstacleGrid[i-1][j]==1 and obstacleGrid[i][j-1]==1:
                    p[i][j] = 0
                elif obstacleGrid[i-1][j]==1:
                    p[i][j] = p[i][j - 1]
                elif obstacleGrid[i][j-1]==1:
                    p[i][j] = p[i - 1][j]
                else:
                    p[i][j] = p[i][j - 1] + p[i - 1][j]
        return p[m-1][n-1]

if __name__ == '__main__':
    class_UP = UniquePaths()
    obstacleGrid = [[0,0,0], [0,1,0], [0,0,0]]
    print(class_UP.uniquePaths(obstacleGrid))