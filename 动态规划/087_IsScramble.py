#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/26 9:29 上午
# @Author : xiongtao
# @File : 087_IsScramble.py 
# @Title : 87. 扰乱字符串

'''
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
下图是字符串 s1 = "great" 的一种可能的表示形式。
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。
同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。
给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

输入: s1 = "great", s2 = "rgeat"
输出: true
'''

'''
题解：动态规划
对于字符串s1和s2，都可以任意拆分为两部分，s1->(s11,s12)，s2->(s21,s22)。
如果s2是s1的扰乱字符串，那么存在以下两种情况：
1. isScramble(s11, s21) and isScramble(s12, s22)
2. isScramble(s11, s22) and isScramble(s12, s21)
以上两种情况任意一种成立，就说明s2是s1的扰乱字符串。

'''

class IsScramble:
    def iScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        # i 表示拆分为第一部分的长度
        for i in range(1, len(s1)):
            if (self.iScramble(s1[:i], s2[:i]) and self.iScramble(s1[i:], s2[i:])) or \
                    (self.iScramble(s1[:i], s2[-i:]) and self.iScramble(s1[i:], s2[:-i])):
                return True
        return False

if __name__ == '__main__':
    class_IS = IsScramble()
    s1 = "abb"
    s2 = "bba"
    print(class_IS.iScramble(s1, s2))