#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/23 8:43 上午
# @Author : xiongtao
# @File : 084_LargestRectangleArea.py 
# @Title : 84. 柱状图中最大的矩形

'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

输入: [2,1,5,6,2,3]
输出: 10
'''

'''
题解：
遍历整个数组heights，计算以heights[i]为右边界的最大面积。

暴力方法：
    1. 对于每个heights[i]，从i开始遍历i之前的元素j，计算[j,i]之间的面积（最小高度*宽度）；
    2. 保留每次计算的最大面积。时间复杂度O(n^2)
修改暴力方法：
    1. 我们没有必要对每个heights[i]都计算一次，只需要对每次递增的峰值进行计算即可（峰值就是比右边元素大的值）；
    2. 原因是因为，若元素a[i]是峰值，即a[i] >= a[i-1]，那么以a[i]为右边界的最大面积 >= 以a[i-1]为右边界的最大面积；

单调递增栈法：
    1. 是否只遍历一次数组就找到最大的矩形面积呢？遍历数组中元素nums[i]，计算以nums[i]为高度的矩形最大面积，
    那么就需要确定以nums[i]为高度的矩形的最大宽度，即矩形的左右边界。
    2. 如何确定nums[i]的右边界？
        如果nums[i+1]<nums[i]，那么我们可以马上断定以nums[i]为高度的矩形的右边界就是nums[i+1]；
        如果nums[i+1]>nums[i]，那么我们不能判断nums[i]的右边界，对于遍历过程中无法判断右边界的高度，我们用数组A存起来(存的元素的下标)。
            数组A中元素对应的高度一定是单调递增的。如果不单调，那么一定存在nums[A[i]]>nums[A[i+1]]，可知A[i]的右边界就是A[i+1]，与数组A的定义矛盾了。
    3. 继续遍历数组nums[j]，将nums[j]与A中元素从右到左对比：
        若nums[j]>nums[A[-1]]，说明nums[j]不是A中元素的右边界，并且nums[j]本身也无法判断右边界，将nums[j]加入到数组A中;
        若nums[j]<nums[A[-1]]，说明nums[j]是A中所有大于nums[j]的元素的右边界，将这些元素一一移出数组并计算相应的最大矩形面积，最后将将nums[j]加入到数组A中;
    4. 如何确定移除数组元素的左边界？
        这个时候大家就会问，上面你只求了右边界，还没说怎么求左边界呢，没有左边界怎么算矩形的面积？
        其实在上面的递增数组中就已经有了A[i]的左边界了，我们知道数组A是单调递增的，nums[A[i-1]] < nums[A[i]]，那么A[i]的左边界就是A[i-1]啦。
        当然A中可能有连续相同高度的元素，对于相同高度我们只计算最后一个的面积，因为相同连续高度的面积都一样。
    5. 如何计算面积？
        假设数组遍历到元素k，且nums[k]<nums[A[i]]，那么nums[A[i]]高度对应的最大矩形面积 = (k - A[i] - 1) * nums[A[i]]
        如果数组中只剩一个元素，说明排在这个元素之前的元素一定比它大(因为数组中的元素只有遇到比自身小的数才会移除数组)，那么对应的最大矩形面积 = A[-1] * i
    6. 为什么是用单调递增栈？
        由上面的数组用到的操作可知，每次输入都是在数组尾部添加，移除数据也是尾部，很符合栈的先进后出的性质。
'''

class LargestRectangleArea:
    # 修改的暴力方法
    def largestRectangleArea(self, heights):
        max_Area = 0
        for i in range(len(heights)):
            # 确定是否是峰值
            if (i < len(heights) - 1 and heights[i] > heights[i + 1]) or i == len(heights) - 1:
                # 计算以i为右边界的最大面积
                min_num = heights[i]
                for j in range(i, -1, -1):
                    # 计算[j,i]之间的最小值
                    min_num = min(min_num, heights[j])
                    max_Area = max(max_Area, min_num * (i - j + 1))
        return max_Area

    # 单调栈方法
    def largestRectangleArea_2(self, heights):
        if len(heights) <= 0:
            return 0
        max_Area = 0
        # 定义数组A并初始化
        A = []
        for i in range(0, len(heights)):
            # 找到右边界
            while len(A) > 0 and heights[i] < heights[A[-1]]:
                curr_height = heights[A[-1]]
                A = A[0:-1]
                # 与当前高度一样的不用在计算
                while len(A) > 0 and curr_height == heights[A[-1]]:
                    A = A[0:-1]
                # 判断是否是数组A中最后一个元素
                if len(A) > 0:
                    max_Area = max(max_Area, (i - A[-1] - 1) * curr_height)
                else:
                    max_Area = max(max_Area, i * curr_height)
            A.append(i)

        # 计算数组A中剩余元素的面积
        while len(A) > 0:
            curr_height = heights[A[-1]]
            A = A[0:-1]
            # 与当前高度一样的不用在计算
            while len(A) > 0 and curr_height == heights[A[-1]]:
                A = A[0:-1]
            # 判断是否是数组A中最后一个元素
            if len(A) > 0:
                max_Area = max(max_Area, (len(heights) - A[-1] - 1) * curr_height)
            else:
                max_Area = max(max_Area, len(heights) * curr_height)
        return max_Area

if __name__ == '__main__':
    class_LRA = LargestRectangleArea()
    heights = [987654321]
    print(class_LRA.largestRectangleArea_2(heights))