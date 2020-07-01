#!/usr/bin python
# -*- coding:UTF-8 -*-
import numpy as np

import random

'''
题目:  数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
'''

class FindKthLargest():

    '''
    解法1：采用K个元素的数组存最大的K个数
    时间复杂度：O(KN)
    等价于部分排序（选择排序或交换排序）
    '''

    # 返回数组中最小值的下标
    def findMinIndex(self, nums):
        index = 0
        min_num = nums[index]
        for i, val in enumerate(nums):
            if min_num > val:
                index = i
                min_num = val
        return index
    def findkthLargest(self, nums, k):
        top_k_nums = []
        top_k_min = float("inf")
        top_k_min_index = None
        num = 0
        for val in nums:
            if len(top_k_nums) < k:
                if val < top_k_min:
                    top_k_min = val
                    top_k_min_index = num
                top_k_nums.append(val)
                num += 1
            elif top_k_min < val:
                top_k_nums[top_k_min_index] = val
                top_k_min_index = self.findMinIndex(top_k_nums)
                top_k_min = top_k_nums[top_k_min_index]
        return top_k_min

    '''
    解法2: 快速排序方法
    时间复杂度：O(nlogn)
    '''
    def partition(self, nums, left, right):
        # 注意可以取到right-1
        index = random.randint(left, right-1)
        nums[left], nums[index] = nums[index], nums[left]
        # nums[left]:主元
        # (left, pos]中的元素都大于等于主元
        # (pos, i-1]中的元素都小于主元
        pos = left
        for i in range(left + 1, right):
            if nums[i] >= nums[left]:
                pos += 1
                if i != pos:
                    nums[pos], nums[i] = nums[i], nums[pos]
        nums[left], nums[pos] = nums[pos], nums[left]
        return nums, pos

    def quickSort(self, nums, left, right):
        if left < right:
            nums, pos = self.partition(nums, left, right)
            nums = self.quickSort(nums, left, pos)
            nums = self.quickSort(nums, pos+1, right)
        return nums

    def findkthLargest_2(self, nums, k):
        nums = self.quickSort(nums, 0, len(nums))
        return nums[k-1]

    '''
    解法3：改进的快速排序方案
    '''
    def findkthLargest_3(self, nums, k):
        left = 0
        right = len(nums)
        while True:
            nums, pos = self.partition(nums, left, right)
            if (pos+1) == k:
                return nums[pos]
            elif (pos+1) < k:
                left = pos+1
            else:
                right = pos
        return left


if __name__ == '__main__':

    '''
    测试用例：3,2,1,5,6,4
    1. 输入: [3,2,1,5,6,4] 和 k = 2
       输出: 5
    2. 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
       输出: 4
    '''

    FKL = FindKthLargest()
    print(FKL.findkthLargest_3([3,2,1,5,6,4], 2))


