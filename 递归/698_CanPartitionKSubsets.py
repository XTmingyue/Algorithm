#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/27 11:46 下午
# @Author : xiongtao
# @File : 698_CanPartitionKSubsets.py 
# @Title : 698. 划分为k个相等的子集

'''
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
'''

# 对数据nums排序后，每次将nums中的一个数任意放置在k个桶中的一个，然后判断剩下的数任意放置是否能够使得K个桶中的和都相等。

# 定义递归函数，将nums中curr位置的数放到memo中是否满足各个桶的和相等
def search(nums, memo, k, curr):
    # 从nums后往前遍历
    if curr < 0:
        return True
    for i in range(0, k):
        # 如果当前的箱子刚好可以放下curr位置的数
        # 或者可以放下curr位置的数，并且还要能放下nums中最小的数，否则可以直接返回当前的放置方法是不满足的
        if nums[curr] == memo[i] or (curr > 0 and memo[i] - nums[curr] >= nums[0]):
            memo[i] = memo[i] - nums[curr]
            # 确定当前curr的放置位置后，其他的数任意放置是否满足要求
            if search(nums, memo, k, curr-1):
                return True
            memo[i] = memo[i] + nums[curr]
    return False

def canPartitionKSubsets(nums, k):
    if sum(nums)/k != sum(nums) // k:
        return False
    # 定义k个桶
    memo = [sum(nums)//k] * k
    nums = sorted(nums)
    return search(nums, memo, k, len(nums)-1)


if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(canPartitionKSubsets(nums, k))
