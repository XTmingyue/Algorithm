#!/usr/bin python
# -*- coding: utf-8 -*- 

# @Time : 2020/7/11 5:35 PM 
# @Author : xiongtao
# @File : 031_NextPermutation.py

'''
题目：实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''
import math

class NextPermutation():
    def Reverse(self, nums, left, right):
        length = math.floor((right - left)/2)
        for i in range(0, length):
            nums[left], nums[right-1] = nums[right-1], nums[left]
            left += 1
            right -= 1
        return nums
    def next_permutation(self, nums):
        index = None
        for i in range(len(nums)-1, 0, -1):
            if i > 0 and nums[i - 1] < nums[i]:
                index = i - 1
                break
        if index == None:
            return self.Reverse(nums, 0, len(nums))
        elif index == len(nums) - 1:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            return nums
        else:
            mark_index = None
            for j in range(len(nums)-1, 0, -1):
                if nums[j] > nums[index]:
                    mark_index = j
                    break
            nums[index], nums[mark_index] = nums[mark_index], nums[index]
            return self.Reverse(nums, index+1, len(nums))


if __name__ == '__main__':
    nums = [1, 2, 3, 5, 4, 3, 2, 1]
    NP = NextPermutation()
    print(NP.next_permutation(nums))
