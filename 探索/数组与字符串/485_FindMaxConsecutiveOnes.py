#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/25 11:34 下午
# @Author : xiongtao
# @File : 485_FindMaxConsecutiveOnes.py 
# @Title : 485. 最大连续1的个数

'''
给定一个二进制数组， 计算其中最大连续1的个数。

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
'''
def findMaxConsecutiveOnes(nums):
    # 记录当前连续1的个数
    count = 0
    # 记录最大的连续1的个数
    max_counts = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            count += 1
            max_counts = max(max_counts, count)
        else:
            count = 0
    return max_counts

def findMaxConsecutiveOnes_2(nums):
    return max(map(len, ''.join(map(str, nums)).split('0')))



if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    print(findMaxConsecutiveOnes_2(nums))