#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/23 11:34 下午
# @Author : xiongtao
# @File : 028_StrStr.py 
# @Title : 28. 实现 strStr()

'''
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

输入: haystack = "hello", needle = "ll"
输出: 2

输入: haystack = "aaaaa", needle = "bba"
输出: -1

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
'''

class StrStr():
    # 暴力搜索(超时)
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        start = -1
        for i in range(0, len(haystack)):
            is_find = 1
            index = i
            for j in range(0, len(needle)):
                if index >= len(haystack) or haystack[index] != needle[j]:
                    is_find = 0
                    break
                index += 1
            if is_find and j == len(needle) - 1:
                start = i
                break
        return start

    # 子串直接比较法
    '''
    时间复杂度：O((n-l)l) l为子串的长度
    空间复杂度：O(1)
    '''
    def strStr_2(self, haystack, needle):
        h_len, n_len = len(haystack), len(needle)
        for i in range(0, (h_len - n_len + 1)):
            if haystack[i:i + n_len] == needle:
                return i
        return -1

if __name__ == '__main__':
    SS = StrStr()
    haystack = "mississippi"
    needle = "mississippi"
    print(SS.strStr_2(haystack, needle))



