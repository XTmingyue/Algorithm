#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/9 8:07 下午
# @Author : xiongtao
# @File : 096_NumTrees.py 
# @Title : 96. 不同的二叉搜索树

'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Solution:
    # 动态规划
    def numTrees(self, n):
        # 定义数组dp[i] 表示长度为i的序列组成的二叉搜索树的个数
        dp = [0] * (n+1)
        # 长度为0和1的序列组成的个数都为1
        dp[0], dp[1] = 1, 1
        # 对于其他长度的序列，可以通过遍历元素拆分为左右子树
        for i in range(2, n+1):
            # 遍历长度为i的元素
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]


if __name__ == '__main__':
    class_S = Solution()
    n = 19
    print(class_S.numTrees(n))

