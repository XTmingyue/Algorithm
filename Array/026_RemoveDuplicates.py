#!/usr/bin python
# -*- coding: utf-8 -*- 

# @Time : 2020/7/8 5:48 PM 
# @Author : xiongtao
# @File : 026_RemoveDuplicates.py

'''
题目：给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

例1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

例2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
'''

class RemoveDuplicates():
    def remove_duplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        # 记录不同数字的个数
        length = 1
        # 遍历数组的下标
        i = 1
        # 记录出现重复数字的第二个位置的下标
        index = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i = i + 1
            else:
                # 将下一个数字覆盖前一个重复的第二个位置
                nums[index] = nums[i]
                i = i + 1
                index += 1
                length += 1
        nums = nums[0:length]
        return length

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    RD = RemoveDuplicates()
    print(RD.remove_duplicates(nums))


