#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/11/26 9:09 上午
# @Author : xiongtao
# @File : 015_ThreeSum.py 
# @Title : 15.三数之和

'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        # 对于两数之和怎么判断？对数组排序后采用左右双指针移动的方法找满足的两个数
        # 对于三数之和，我们也是先进行排序，然后从左到右依次固定数字a，在右边剩下的元素中采用双指针法找b和c
        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = n - 1
            while start < end:
                sum_abc = nums[i] + nums[start] + nums[end]
                if sum_abc == 0:
                    res.append([nums[i], nums[start], nums[end]])
                    while start < n-1 and nums[start] == nums[start+1]:
                        start += 1
                    while end > i and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif sum_abc > 0:
                    end -= 1
                else:
                    start += 1
        return res

if __name__ == '__main__':
    class_S = Solution()
    nums = [-2,0,0,2,2]
    print(class_S.threeSum(nums))