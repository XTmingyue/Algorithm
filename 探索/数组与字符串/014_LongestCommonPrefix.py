#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/20 11:15 下午
# @Author : xiongtao
# @File : 014_LongestCommonPrefix.py
# @title : 14. 最长公共前缀

'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

输入: ["flower","flow","flight"]
输出: "fl"

'''

class LongestCommonPrefix():
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        # 初始化最长公共前缀下标为第一个元素的长度
        len_num = len(strs[0])
        is_have = 0
        for i in range(1, len(strs)):
            # 和前一个字符串是否有相同子串
            signal = 0
            if len(strs[i]) < len_num:
                len_num = len(strs[i])
            for j in range(len_num, 0, -1):
                if strs[i-1][0:j] == strs[i][0:j]:
                    len_num = j
                    # 如果是最后一个字符串，说明找到了最大公共子串
                    if i == len(strs)-1:
                        is_have = 1
                    signal = 1
                    break
            if signal == 0:
                return ""
        if is_have == 0:
            return ""
        return strs[0][0:len_num]

if __name__ == '__main__':
    LCP = LongestCommonPrefix()
    strs = ["b","cb","cab"]
    print(LCP.longestCommonPrefix(strs))