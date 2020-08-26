#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/25 11:49 下午
# @Author : xiongtao
# @File : 209_MinSubArrayLen.py 
# @Title : 209. 长度最小的子数组

'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
如果不存在符合条件的子数组，返回 0。

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
'''

# 双指针法，利用了元素都为正的性质
'''
题解：
定义两个指针start和end，先逐渐累加start～end之间的和，当>=s时记录此时的长度。
由于数组中的都是正数，因此我们从start开始逐渐缩短，将start逐渐右移，同时与s进行比较，记录满足>=s的最短长度。
一旦start～end的和<s时，我们就继续移动end。

证明：当[i, i+k]的和刚好>=s时，如果[i+1, i+k]也>=s，那么以i+1为起点的连续子序列之和要>=s，这个子序列最小一定是[i+1, i+k]
因为如果以i+1为起点的最小>=s的连续子序列比[i+1, i+k]小，假设是[i+1, i+h]，其中h<k。
那么一定有sum[i, i+h] >= s,  而这与[i, i+k]的和刚好>=s相矛盾。
'''
def minSubArrayLen(s, nums):
    if len(nums) == 0:
        return 0
    start = 0
    end = 0
    min_len = len(nums) + 1
    array_sum = nums[0]
    while start <= end and end < len(nums):
        if array_sum < s:
            end += 1
            if end < len(nums):
                array_sum += nums[end]
        elif array_sum >= s:
            min_len = min(min_len, end - start + 1)
            array_sum -= nums[start]
            start += 1
    if min_len == len(nums) + 1:
        return 0
    return min_len

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    s = 15
    print(minSubArrayLen(s, nums))