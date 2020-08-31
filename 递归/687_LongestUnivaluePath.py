#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/26 11:47 下午
# @Author : xiongtao
# @File : 687_LongestUnivaluePath.py 
# @Title : 687. 最长同值路径

'''
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
注意：两个节点之间的路径长度由它们之间的边数表示。

示例：
              5
             / \
            4   5
           / \   \
          1   1   5

输出: 2
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LongestUnivluePath():

    # 定义函数 计算经过当前根节点为 起点 的最长路径 (因为只有是起点才可能将左右两个路径合并，这里为起点的最长路径有可能是右子树，也可能是左子树)
    # 同时使用字段max_len来记录以每一个节点为根结点的最长路径
    def get_longestPath_through_root(self, root:TreeNode):
        if root == None:
            return 0
        # 计算以右子节点、左子节点为起点的最长路径
        left_len = self.get_longestPath_through_root(root.left)
        right_len = self.get_longestPath_through_root(root.right)

        max_left_len = 0
        max_right_len = 0
        # 计算根结点右侧的最长路径
        if root.left != None and root.val == root.left.val:
            max_left_len = left_len + 1
        # 计算根结点右侧的最长路径
        if root.right != None and root.val == root.right.val:
            max_right_len = right_len + 1

        # 记录全局最长路径
        global max_len
        max_len = max(max_len, max_left_len+max_right_len)

        # 返回的是以根结点为起点的最长路径
        return max(max_left_len, max_right_len)

    def longestUnicaluePath(self, root: TreeNode):
        global max_len
        max_len = 0
        self.get_longestPath_through_root(root)
        return max_len

