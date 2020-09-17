#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/8 12:46 上午
# @Author : xiongtao
# @File : 面试题 08.06_Hanota.py 
# @Title : 面试题 08.06. 汉诺塔问题

'''
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。

请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

你需要原地修改栈。

输入：A = [2, 1, 0], B = [], C = []
输出：C = [2, 1, 0]
'''

# 题解：https://leetcode-cn.com/problems/hanota-lcci/solution/tu-jie-yi-nuo-ta-de-gu-shi-ju-shuo-dang-64ge-pan-z/
class Hanota:
    # 将A中N个圆盘移动到C中
    def n_hanota(self, A, B, C, N):
        if N == 1:
            C.append(A[-1])
            A.pop()
            return
        else:
            # 将前N-1个数移动到B中
            self.n_hanota(A, C, B, N-1)
            # 将最后一个数移动到C中
            C.append(A[-1])
            A.pop()
            # 将B中的数移动到C中
            self.n_hanota(B, A, C, N-1)
    def hanota(self, A, B, C):
        """
        Do not return anything, modify C in-place instead.
        """
        self.n_hanota(A, B, C, len(A))

