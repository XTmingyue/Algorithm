#!/usr/bin python
# -*- coding: utf-8 -*- 

# @Time : 2020/7/4 4:36 PM 
# @Author : xiongtao
# @File : 015_threeSum.py

'''
题目：给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class ThreeSum():
    '''
    解题方法：
    排序 + 双指针
    本题的难点在于如何去除重复解

    算法流程：
    1. 特判，对于数组长度 n，如果数组为 null 或者数组长度小于 33，返回 []。
    对数组进行排序。
    2. 遍历排序后数组：（以nums[i]为第一个数）
        - 若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
        - 对于重复元素：跳过，避免出现重复解
        - 令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：
            1）当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
            2）若和大于 0，说明 nums[R] 太大，R 左移
            3）若和小于 0，说明 nums[L] 太小，L 右移
    '''
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = len(nums) - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # 找到一个等于0的结果之后，因为数组已经进行了排序，为了避免重复结果
                    # 需要排除相同值的nums[L]和nums[R]
                    while L < R and nums[L] == nums[L+1]:
                        L = L+1
                    while L < R and nums[R] == nums[R-1]:
                        R = R-1
                    # 只要nums[L]!=nums[L+1]，那么nums[i] + nums[L] + nums[R] != 0
                    # 因此要找到等于0的结果，R也要往左移一位
                    L = L+1
                    R = R-1
                elif nums[i] + nums[L] + nums[R] > 0:
                    # 因为 nums[i] + nums[L] + nums[R] != 0，那么就算nums[R] == nums[R-1]
                    # 依旧有 nums[i] + nums[L] + nums[R-1] != 0，不会产生重复的结果
                    R = R-1
                else:
                    L = L+1
        return res

if __name__ == '__main__':
    TS = ThreeSum()
    nums = [-1, 0, 1, 2, -1, -4]
    print(TS.threeSum(nums))