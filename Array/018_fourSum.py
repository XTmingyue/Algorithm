#!/usr/bin python
# -*- coding: utf-8 -*- 

# @Time : 2020/7/5 11:48 PM 
# @Author : xiongtao
# @File : 018_fourSum.py

'''
题目：给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class FourSum():
    '''
    解题思路：
    与计算三个数之和等于某个值的逻辑一致。先进行排序，四个数的下标依次为a、b、c、d.
    遍历数组依次作为第一个数a，然后在剩下的数组中寻找b/c/d之和为target-nums[a]

    通过一些剪枝操作，即判断某些情况出现之后就不需要继续遍历，可以有效减少程序的运行时间。

    时间复杂度：O(N^3)
    '''
    def four_sum(self, nums, target):
        if len(nums) < 4:
            return []
        res = []
        nums.sort()
        for a in range(0, len(nums) - 3):
            # 去重 注意用if 而不是while
            if a > 0 and nums[a] == nums[a-1]:
                continue
            # 剪枝
            if nums[a] + 3 * nums[a+1] > target:
                return res
            if nums[a] + 3 * nums[-1] < target:
                continue
            for b in range(a+1, len(nums)-2):
                # 去重
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                # 剪枝
                if nums[a] + nums[b] + 2*nums[b+1] > target:
                    continue
                if nums[a] + nums[b] + 2*nums[-1] < target:
                    continue
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c+1]:
                            c = c + 1
                        while c < d and nums[d] == nums[d-1]:
                            d = d - 1
                        c = c + 1
                        d = d - 1
                    elif sum > target:
                        d = d - 1
                    else:
                        c = c + 1
        return res

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    target = -1
    FS = FourSum()
    print(FS.four_sum(nums, target))