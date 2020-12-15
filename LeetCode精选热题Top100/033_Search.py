#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/12/4 8:58 上午
# @Author : xiongtao
# @File : 033_Search.py 
# @Title : 33. 搜索旋转排序数组

'''
给你一个整数数组 nums ，和一个整数 target 。
该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。
请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
'''

class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            if start == end and nums[start] == target:
                return start
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] >= nums[0]:
                    if target < nums[mid] and target >= nums[0]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if target > nums[mid] and target <= nums[-1]:
                        start = mid + 1
                    else:
                        end = mid - 1
        return -1


if __name__ == '__main__':
    class_S = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(class_S.search(nums, target))
