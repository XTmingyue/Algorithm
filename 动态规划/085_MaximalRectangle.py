#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/22 8:42 上午
# @Author : xiongtao
# @File : 085_MaximalRectangle.py 
# @Title : 85. 最大矩形

'''
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
'''

class MaxRectangle:
    def maxRectangle(self, matrix):
