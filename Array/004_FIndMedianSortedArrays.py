#!/usr/bin python
# -*- coding: utf-8 -*- 

# @Time : 2020/7/1 7:48 PM 
# @Author : xiongtao
# @File : 004_FIndMedianSortedArrays.py
'''

题目：给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
'''

import math

class FindMedianSortedArrays():
    def findMedianSortedArrays(self, nums1, nums2):
        merge = []
        index1 = 0
        index2 = 0
        for i in range(0, len(nums1) + len(nums2)):
            if index1 < len(nums1) and index2 < len(nums2):
                if nums1[index1] <= nums2[index2]:
                    merge.append(nums1[index1])
                    index1 += 1
                elif nums1[index1] > nums2[index2]:
                    merge.append(nums2[index2])
                    index2 += 1
            else:
                break
        if index1 >= len(nums1):
            merge.extend(nums2[index2:])
        else:
            merge.extend(nums1[index1:])

        pos = (len(nums1) + len(nums2)) / 2

        if pos != round(pos):
            return merge[math.floor(pos)]
        else:
            return (merge[int(pos)] + merge[int(pos) - 1]) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    FMSA = FindMedianSortedArrays()
    print(FMSA.findMedianSortedArrays(nums1, nums2))