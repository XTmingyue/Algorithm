#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/3 10:25 下午
# @Author : xiongtao
# @File : 794_ValidTicTacToe.py 
# @Title : 794. 有效的井字游戏

'''
用字符串数组作为井字游戏的游戏板 board。当且仅当在井字游戏过程中，玩家有可能将字符放置成游戏板所显示的状态时，才返回 true。

该游戏板是一个 3 x 3 数组，由字符 " "，"X" 和 "O" 组成。字符 " " 代表一个空位。

以下是井字游戏的规则：

玩家轮流将字符放入空位（" "）中。
第一个玩家总是放字符 “X”，且第二个玩家总是放字符 “O”。
“X” 和 “O” 只允许放置在空位中，不允许对已放有字符的位置进行填充。
当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
当所有位置非空时，也算为游戏结束。
如果游戏结束，玩家不允许再放置字符。

示例 1:
输入: board = ["O  ", "   ", "   "]
输出: false
解释: 第一个玩家总是放置“X”。

示例 2:
输入: board = ["XOX", " X ", "   "]
输出: false
解释: 玩家应该是轮流放置的。

示例 3:
输入: board = ["XXX", "   ", "OOO"]
输出: false

示例 4:
输入: board = ["XOX", "O O", "XOX"]
输出: true
'''

# 生效的几个必要条件：
# 1. X的数量一定大于等于O的数量；
# 2. X获胜，则X的个数比O多一个； O获胜，则O的数量和X一致；
# 3. 游戏板上不可能同时出现3个X在一行且3个O在一行的情况；
class ValidTicTacToe:
    # 定义获胜函数，判断当前用户是否胜利
    def is_win(self, board, signal):
        if (board[0][0] == board[1][1] == board[2][2] == signal) or \
                (board[0][2] == board[1][1] == board[2][0] == signal):
            return True
        for i in range(0, 3):
            # 一行是否都相同
            if board[i].count(signal) == 3:
                return True
            # 一列是否都相同
            if all(board[j][i] == signal for j in range(0, 3)):
                return True
        return False

    def validticTacToe(self, board):
        signal_1 = 'X'
        signal_2 = 'O'
        x_count = sum(row.count(signal_1) for row in board)
        o_count = sum(row.count(signal_2) for row in board)

        if o_count not in (x_count, x_count-1):
            return False
        if self.is_win(board, signal_1) and x_count != o_count + 1:
            return False
        if self.is_win(board, signal_2) and x_count != o_count:
            return False
        return True

if __name__ == '__main__':
    class_valid = ValidTicTacToe()
    board = ["XO ","XO ","XO "]
    print(class_valid.validticTacToe(board))