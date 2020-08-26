#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/23 11:12 下午
# @Author : xiongtao
# @File : 151_ReverseWords.py 
# @Title : 151.翻转字符串里的单词

'''
给定一个字符串，逐个翻转字符串中的每个单词。
输入: "the sky is blue"
输出: "blue is sky the"

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
'''

class ReverseWords():
    def reverseStr(self, str):
        str = list(str)
        str_len = len(str) - 1
        for i in range(0, len(str)//2):
            str[i], str[str_len - i] = str[str_len - i], str[i]
        return ''.join(str)
    def reverseWords(self, s):
        s = self.reverseStr(s)
        strs = s.strip().split(" ")
        for i in range(0, len(strs)):
            strs[i] = self.reverseStr(strs[i])
        res = ''
        for str in strs:
            if str != '':
                res = res + str + ' '
        return res[:-1]
    def reverseWords_2(self, s):
        # split()函数默认可以按空格分割，并且把结果中的空字符串删除掉
        return " ".join(reversed(s.split()))

if __name__ == '__main__':
    RW = ReverseWords()
    s = "a good   example"
    print(RW.reverseWords_2(s))
