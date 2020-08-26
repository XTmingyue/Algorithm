#!/usr/bin python
# -*- coding: utf-8 -*- 

# @Time : 2020/7/11 4:54 PM 
# @Author : xiongtao
# @File : 027_RemoveElement.py

'''
题目：给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

例子：
给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。

'''

class RemoveElement():
    def remove_element(self, nums, val):
        # index 指向第一个等于val的数组下标
        index = None
        ele_num = 0
        for i in range(0, len(nums)):
            if nums[i] != val and index != None:
                nums[index] = nums[i]
                ele_num += 1
                index += 1
            elif nums[i] == val and index == None:
                index = i
            elif nums[i] != val:
                ele_num += 1
        print(nums[0:ele_num])
        return ele_num

    # 采用快慢双指针的方式
    def remove_element_2(self, nums, val):
        # slow和fast同时往前移动，当遇到等于val的值时，slow不动，fast继续移动找到下一个不等于val的值，将其替换到slow的位置
        slow = 0
        for fast in range(0, len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    RE = RemoveElement()
    print(RE.remove_element_2(nums, val))
