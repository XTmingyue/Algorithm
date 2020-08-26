#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/24 11:30 下午
# @Author : xiongtao
# @File : 561_ArrayPairSum.py 
# @Title : 561. 数组拆分 I

'''
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

输入: [1,4,3,2]
输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).

证明：min{}数对必是有序数列上相邻元素
https://leetcode-cn.com/problems/array-partition-i/solution/minshu-dui-bi-shi-you-xu-shu-lie-shang-xiang-lin-y/
定义有序数对 (ai,bi)，其中ai<bi。我们要使得sum(ai), i=1,2,3...,n 最大。
sum(bi-ai) = sum(bi) - sum(ai)
又由于sum(ai)+sum(bi) = L(数组之和，为定值)
那么 sum(bi-ai)=sum(bi) - sum(ai)=L-2sum(ai)
我们要使得max sum(ai)就等价于使得min sum(bi-ai)，由于bi>ai，也就是对于每一个数对(ai,bi)都有min (bi-ai)
那么ai和bi就是排序数组相邻的两个元素。
'''

class ArrayPairSum():
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])

if __name__ == '__main__':
    APS = ArrayPairSum()
    nums = [1,4,3,2]
    print(APS.arrayPairSum(nums))