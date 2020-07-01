#!/usr/bin python
# -*- coding: UTF-8 -*-

'''
题目:  两数之和等于某个固定的数
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class TowSum():
    '''
    -- 穷举
    '''
    def twoSum_1(self, nums, target):
        res = []
        for i, val_i in enumerate(nums):
            for j, val_j in enumerate(nums):
                if (i!=j and val_i + val_j == target):
                    res.extend([i, j])
                    return res
        return res
    '''
    -- Dict/HashTable
    '''
    def twoSum_2(self, nums, target):
        res = []
        nums_dict = dict()
        # 将nums转换为dict
        for i, val in enumerate(nums):
            nums_dict['%d' % val] = i
        for i, val in enumerate(nums):
            left_num = target - val
            if ('%d' % left_num) in nums_dict.keys() and nums_dict['%d' % left_num] != i:
                res.extend([i, nums_dict['%d' % left_num]])
                return res
        return res

if __name__ == '__main__':
    TS = TowSum()
    print(TS.twoSum_2([2, 7, 11, 15], 9))

