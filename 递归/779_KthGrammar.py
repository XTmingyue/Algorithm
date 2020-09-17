#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/1 11:04 下午
# @Author : xiongtao
# @File : 779_KthGrammar.py 
# @Title : 779. 第K个语法符号

'''
在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。

给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）

输入: N = 1, K = 1
输出: 0

输入: N = 2, K = 1
输出: 0

输入: N = 2, K = 2
输出: 1

输入: N = 4, K = 5
输出: 1

解释:
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001
'''

class KthGrammar:
    def kth_delta_str(self, str_nums, N):
        if N == 0:
            return str_nums
        str_nums = ['01' if x=='0' else '10' for x in str_nums]
        return self.kth_delta_str(list(''.join(str_nums)), N-1)
    # 暴力
    def kthGrammar(self, N, K):
        str_nums = ['0']
        str_nums = self.kth_delta_str(str_nums, N-1)
        print(str_nums)
        return str_nums[K-1]

    # 第 K 个数字是上一行第 (K+1) / 2 个数字生成的
    def kthGrammar_2(self, N, K):
        if N == 1:
            return 0
        last_num = self.kthGrammar_2(N - 1, (K + 1) // 2)
        if last_num == 0:
            if K % 2 == 0:
                return 1
            else:
                return 0
        else:
            if K % 2 == 0:
                return 0
            else:
                return 1

if __name__ == '__main__':
    class_kth = KthGrammar()
    N = 3
    K = 4
    print(class_kth.kthGrammar_2(N, K))

