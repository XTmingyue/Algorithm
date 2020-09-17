#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/10 11:50 下午
# @Author : xiongtao
# @File : 010_IsMatch.py 
# @Title : 10. 正则表达式匹配

'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
'''

'''
题解：采用动态规划进行求解，首先我们要考虑当前问题可以拆分为怎么的子问题，求出对应的转移方程。
我们定义如下数组：m[i][j] 表示字符串s前i个字符与字符规律p前j个字符是否匹配。
此时存在两种情况：
1. p[j] != '*'
    那么如果s[i]==p[j]或者p[j] == '.'，只需要判断m[i-1][j-1]是否为True；
    否则如果s[i] != p[j]且p[j] != '.'，那么m[i][j] == False
2. p[j] == '*'
    我们要先判断s[i] == p[j-1]？
        如果s[i] != p[j-1] 那么'*'代表的是一定是0个，只需要要判断m[i][j-2]是否为True。
        如果s[i] == p[j-1] 那么'*'即可以代表0个，也可以代表任意多个，我们需要判断 m[i][j-2] 或者 m[i-1][j] 是否为True；
m[i][j]的初始化是[len(s)+1, len(p)+1]，m[0][0]=True表示两个空字符串是匹配的。这样定义的好处是避免边界判断
'''

class IsMatch:
    # 注意判断临界值
    def match(self, s, s_index, p, p_index):
        if s_index < 0:
            return False
        if p[p_index] == '.':
            return True
        return s[s_index] == p[p_index]
    def isMatch(self, s, p):
        len_s = len(s)
        len_p = len(p)
        # 初始化转移矩阵
        # m[i][j] 表示字符串s前i个字符与字符规律p前j个字符是否匹配
        m = [[False] * (len_p+1) for i in range(0, len_s+1)]
        m[0][0] = True
        # i  表示s中前i个字符
        # j 表示p中前j个字符
        for i in range(0, len_s+1):
            for j in range(1, len_p+1):
                # p中第j个字符是否为*
                if p[j-1] != '*':
                    # 由于i从0开始，在match中注意判断临界值
                    if self.match(s, i-1, p, j-1):
                        m[i][j] = m[i-1][j-1]
                else:
                    if self.match(s, i-1, p, j-2):
                        m[i][j] = m[i-1][j] or m[i][j-2]
                    else:
                        m[i][j] = m[i][j-2]
        return m[len_s][len_p]

if __name__ == '__main__':
    s = ""
    p = ".*"
    class_is_match = IsMatch()
    print(class_is_match.isMatch(s, p))