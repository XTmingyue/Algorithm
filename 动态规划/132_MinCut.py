#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/14 8:32 上午
# @Author : xiongtao
# @File : 132_MinCut.py 
# @Title : 132. 分割回文串 II

'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回符合要求的最少分割次数。

示例:
输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
'''

class MinCut:
    def minCut(self, s):
