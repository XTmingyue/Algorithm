#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/20 10:13 下午
# @Author : xiongtao
# @File : 498_FindDiagonalOrder.py

'''
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

'''

class FindDiagonalOrder():
    def findDiagonalOrder(self, matrix):
        if len(matrix)==0:
            return []
        # 指示遍历的方向，1表示斜向左下，0表示斜向右上
        signal = 0
        curr_row = 0
        curr_col = 0
        row_num = len(matrix) - 1
        col_num = len(matrix[0]) - 1
        res = []
        while curr_row <= row_num and curr_col <= col_num:
            res.append(matrix[curr_row][curr_col])
            if signal == 1:
                if curr_col == 0 and curr_row < row_num:
                    curr_row += 1
                    signal = 0
                elif curr_row == row_num:
                    curr_col += 1
                    signal = 0
                else:
                    curr_row += 1
                    curr_col -= 1
            else:
                if curr_row == 0 and curr_col < col_num:
                    curr_col += 1
                    signal = 1
                elif curr_col == col_num:
                    curr_row += 1
                    signal = 1
                else:
                    curr_row -= 1
                    curr_col += 1
        return res


if __name__ == '__main__':
    FDO = FindDiagonalOrder()
    matrix = [[ 1, 2, 3 ],
              [ 4, 5, 6 ],
              [ 7, 8, 9 ]]
    print(FDO.findDiagonalOrder(matrix))