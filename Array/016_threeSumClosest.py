#!/usr/bin python
# -*- coding: utf-8 -*- 

# @Time : 2020/7/4 8:03 PM 
# @Author : xiongtao
# @File : 016_threeSumClosest.py

'''
Q:给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
'''

class ThreeSumClosest():
    '''
    解题思路：
    与上面的求数组中三个值之和为某个值的思路一致，都是先进行排序，然后假设nums[i]为三个数的第一个，另外两个指针L、R分别指向后两个。
    而L/R每次的移动方向都是想着逼近target的方向移动。
    '''
    def update(self, target, cur, best):
        if abs(cur - target) < abs(best - target):
            return cur
        return best
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return None
        nums.sort()
        best = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = len(nums) - 1
            while L < R:
                cur = nums[i] + nums[L] + nums[R]
                if cur == target:
                    return target
                best = self.update(target, cur, best)
                if cur < target:
                    # 去掉一样的值，加快执行速度
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    L = L+1
                else:
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    R = R-1
        return best

if __name__ == '__main__':
    nums = [-1,0,1,1,55]
    target = 3
    TSC = ThreeSumClosest()
    print(TSC.threeSumClosest(nums, target))
