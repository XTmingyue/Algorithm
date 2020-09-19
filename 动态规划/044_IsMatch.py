#!/usr/bin python
# -*- coding: utf-8 -*- 

# @Time : 2020/9/18 2:11 PM 
# @Author : xiongtao
# @File : 044_IsMatch.py
# @Title : 44. 通配符匹配


'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
'''

'''
题解：参考010题 正则表达式匹配。采用动态规划进行求解。
定义数组m[i][j]：字符串s前i个字符与字符串p前j个字符是否匹配。d[0][0]=True：表示空字符串是匹配的。
要判断m[i][j]? 区分以下两种情况：
1. p[j] == '*':
    由于'*'既可以表示匹配空字符串，又可以匹配若干个字符串。因此m[i][j] = m[i][j-1] or m[i-1][j]
2. p[j] != '*'
    只需要判断s[i]与p[j]是否匹配，若匹配，则m[i][j] = m[i-1][j-1];否则m[i][j]=False

'''
class Sloution:
    def strMatch(self, s, p, index1, index2):
        if index1 < 0:
            return False
        if p[index2] == '?':
            return True
        return s[index1] == p[index2]

    def isMatch(self, s, p):
        # 初始化数组
        m = [[False] * (len(p)+1) for _ in range(0, len(s)+1)]
        m[0][0] = True
        for i in range(0, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    m[i][j] = m[i][j - 1]
                    if i > 0:
                        m[i][j] = m[i][j] or m[i-1][j]
                else:
                    if self.strMatch(s, p, i-1, j-1):
                        m[i][j] = m[i - 1][j - 1]
        return m[len(s)][len(p)]


if __name__ == '__main__':
    class_s = Sloution()
    s = "adceb"
    p = "*a*b"
    print(class_s.isMatch(s, p))