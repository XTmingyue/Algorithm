#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/23 8:16 上午
# @Author : xiongtao
# @File : 174_CalculateMinimumHP.py 
# @Title : 174. 地下城游戏

'''
一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。
我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
为了尽快到达公主，骑士决定每次只向右或向下移动一步。

编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
'''

class Solution:
    '''
    题解：动态规划
    一般处理二维的动态规划问题需要定义二维数组，这里我们不能定义dp[i][j]是[0][0]到[i][j]的最小初始健康值。
    因为我们分析后会发现要计算dp[i][j]时，不仅要[i][j-1]、[i-1][j]时刻的最小初始健康值，还要有到[i][j-1]、[i-1][j]时刻累计路径和。

    故，我们假设dp[i][j]是[i][j]到终点所需要的最小初始健康值。
    那么，假设已知dp[i+1][j]和dp[i][j+1]，骑士到达[i+1][j]或[i][j+1]的初始值为dp[i][j] + dungeon[i][j]
    只要dp[i][j] + dungeon[i][j] = min(dp[i+1][j], dp[i][j+1])，骑士就可以达到终点。
    因此 dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
    需要注意的是初始值必须大于等于1，因为骑士在终点时的健康值至少要是1，否则为0就死亡了。
    '''
    def calculateMinimumHP(self, dungeon):
        if len(dungeon) == 0:
            return 0
        n, m = len(dungeon), len(dungeon[0])
        dp = [[0] * m for _ in range(n)]
        if dungeon[n-1][m-1] == 0:
            dp[n-1][m-1] = 1
        elif dungeon[n-1][m-1] < 0:
            dp[n - 1][m - 1] = 1 + (-1 * dungeon[n-1][m-1])
        # 初始化第n行
        for j in range(m-2, -1, -1):
            dp[n-1][j] = dp[n-1][j+1] - dungeon[n-1][j]
        for i in range(n-2, -1, -1):
            dp[i][m-1] = dp[i+1][m-1] - dungeon[i][m-1]
        print(dp)



if __name__ == '__main__':
    solution = Solution()
    #dungeon = [[1, -4, 5,-99],[2,-2,-2,-1]]
    dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
    print(solution.calculateMinimumHP(dungeon))