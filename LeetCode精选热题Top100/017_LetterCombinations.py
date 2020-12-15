#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/11/26 9:40 下午
# @Author : xiongtao
# @File : 017_LetterCombinations.py 
# @Title : 17. 电话号码的字母组合

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:
    dict_digits = {'1': [], '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv",
                        '9': "wxyz"}
    # 返回str可能的组合
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(self.dict_digits[digits])
        res = self.letterCombinations(digits[1:])
        curr = []
        for s in list(self.dict_digits[digits[0:1]]):
            for val in res:
                curr.append(s + val)
        return curr

if __name__ == '__main__':
    class_S = Solution()
    digits = "23"
    print(class_S.letterCombinations(digits))

