#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/18 12:01 上午
# @Author : xiongtao
# @File : 035_SearchInsert.py

'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
'''

import math

class SearchInsert():
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            index = math.floor((right+left) / 2)
            if nums[index] == target:
                return index
            elif nums[index] > target:
                right = index - 1
            else:
                left = left + 1
        return left

if __name__ == '__main__':
    SI = SearchInsert()
    nums = [1,3,5,6]
    target = 5
    print(SI.searchInsert(nums, target))