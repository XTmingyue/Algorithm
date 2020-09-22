#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/22 7:31 上午
# @Author : xiongtao
# @File : 072_MinDistance.py 
# @Title : 72. 编辑距离

'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
- 插入一个字符
- 删除一个字符
- 替换一个字符

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
'''

'''
动态规划：
定义数组T[i][j]:表示将word1前i个字符转换为word2前j个字符的最少操作数。分为以下三种情况：
1. 已知T[i][j-1]，要求T[i][j]
    既然已经知道了从word1前i个字符转换为word2前j-1个字符的最少操作数，那么当word2新增了一个字符之后，word1只需要在第i个字符后插入一个同样的字符即可。
    此时，T[i][j] = T[i][j-1] + 1
2. 已知T[i-1][j]，要求T[i][j]
    既然已经知道了从word1前i-1个字符转换为word2前j个字符的最少操作数，那么当word1新增了一个字符之后，只需要将word1第i个字符删除即可。
    此时，T[i][j] = T[i-1][j] + 1
3. 已知T[i-1][j-1]，要求T[i][j]
    既然已经知道了从word1前i-1个字符转换为word2前j-1个字符的最少操作数，那么当word1与word2同时增加一个字符，只需要修改word1新增的，使其与word2新增加的相同即可。
    此时，T[i][j] = T[i-1][j-1] + 1 （如果word1[i] == word2[j]，那么T[i][j] = T[i-1][j-1]）
因为，要计算的是最少操作数，所以T[i][j]的最终值是上述三种方式的最小值。
'''

class MinDistance:
    def minDistance(self, word1, word2):
        # 初始化数组
        T = [[0]*(len(word2)+1) for _ in range(0, len(word1)+1)]
        # 空字符串转换为空字符串的编辑距离为0
        T[0][0] = 0
        # word1为空时，编辑距离为word2的长度
        for i in range(1, len(word2)+1):
            T[0][i] = i
        # word2为空时，编辑距离为word1的长度
        for j in range(1, len(word1)+1):
            T[j][0] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    T[i][j] = min(1 + T[i][j - 1], 1 + T[i - 1][j], T[i - 1][j - 1])
                else:
                    T[i][j] = min(1 + T[i][j - 1], 1 + T[i - 1][j], 1 + T[i - 1][j - 1])
        return T[len(word1)][len(word2)]

if __name__ == '__main__':
    class_MD = MinDistance()
    word1 = "horse"
    word2 = "ros"
    print(class_MD.minDistance(word1, word2))
