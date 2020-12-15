#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/12/9 9:05 上午
# @Author : xiongtao
# @File : 034_SearchRange.py 
# @Title : 34. 在排序数组中查找元素的第一个和最后一个位置

'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 
示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
'''

class Solution:
    def binarySearchLeft(self, nums, target):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            if start == end and nums[start] == target:
                return start
            mid = (start + end) // 2
            if nums[mid] == target:
                # 找到的target的位置是数组中最左侧的位置时，返回。否则从该位置的前一个位置向左继续寻找
                if mid == 0 or (mid > 0 and nums[mid-1] < target):
                    return mid
                else:
                    end = mid - 1
            else:
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1

    def binarySearchRight(self, nums, target):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            if start == end and nums[start] == target:
                return start
            mid = (start + end) // 2
            if nums[mid] == target:
                # 找到的target的位置是数组中最右侧的位置时，返回。否则从该位置的下一个位置向右继续寻找
                if mid == len(nums) - 1 or (mid < len(nums) - 1 and nums[mid + 1] > target):
                    return mid
                else:
                    start = mid + 1
            else:
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1

    def searchRange(self, nums, target):
        return [self.binarySearchLeft(nums, target), self.binarySearchRight(nums, target)]

if __name__ == '__main__':
    class_S = Solution()
    nums = []
    target = 6
    print(class_S.searchRange(nums, target))