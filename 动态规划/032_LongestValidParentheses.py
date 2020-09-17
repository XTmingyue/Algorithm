#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/15 8:08 上午
# @Author : xiongtao
# @File : 032_LongestValidParentheses.py 
# @Title : 32. 最长有效括号

'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
'''

'''
题解：
采用栈来判断有效括号。如果是'('就入栈，如果是')'就从栈中弹出一个'('，并统计两个括号之间的长度作为有效括号的长度。
但是需要注意一下情况"()()"也是有效括号，但是如果按照栈直接进行计算，最长的有效括号是2。
因此我们要记录一个字段start，该字段表示当前有效括号的起始下标，初始值为0，那么什么时候重新赋值呢？
    1. 当现在的有效括号结束时进行重新赋值，那么什么时候有效括号结束？
    2. 由于栈中存放的都是'('的序号，因此当我们现在遍历到')'时且栈为空，说明找不到匹配了，此时说明有效括号结束了；
    3. 下一个有效括号的起始点一定是'('，因此start设定为遍历到的')'下一个下标；
'''

class Sloution:
    # 使用栈进行求解
    def longestValidParentheses(self, s) -> int:
        s_deque = []
        start = 0
        max_len = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                s_deque.append(i)
            else:
                # 当前是')'且栈为空，切换起始位置
                if len(s_deque) == 0:
                    start = i + 1
                    continue
                else:
                    s_deque.pop()
                    if len(s_deque) > 0:
                        # 与栈顶元素比，避免'(()()'情况计算不准
                        max_len = max(max_len, i - s_deque[-1])
                    else:
                        # 与起始位置比，避免'()()'情况计算不准
                        max_len = max(max_len, i - start + 1)
        return max_len

    # 动态规划求解（https://zhuanlan.zhihu.com/p/41951874）
    # 定义d[i]:以下标i起始的最长有效括号的长度
    # 如果s[i] == '(' 并且 s[d[i+1] + i + 1] == ')'，那么d[i] = d[i+1] + 2。不过此时需要注意以下情形'(())()'
    # 因此在上述情况之上，如果d[i+1] + i + 2还有字符，那么d[i] = d[i] + d[d[i+1] + i + 2]，此时才是最长的有效括号的长度。
    def longestValidParentheses_2(self, s):
        # 定义数组d[i]
        d = [0 for _ in range(len(s))]
        max_len = 0
        # 从右向左遍历字符串
        for i in range(len(s)-2, -1, -1):
            if s[i] == '(':
                left_index = d[i+1] + i + 1
                if left_index < len(s) and s[left_index] == ')':
                    d[i] = d[i+1] + 2
                    if (left_index + 1) < len(s):
                        d[i] += d[left_index + 1]
            max_len = max(max_len, d[i])
        return max_len

if __name__ == '__main__':
    class_s = Sloution()
    s = "(((()(()"
    print(class_s.longestValidParentheses_2(s))


