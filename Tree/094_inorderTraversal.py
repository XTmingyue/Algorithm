#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/11 11:30 下午
# @Author : xiongtao
# @File : 094_inorderTraversal.py

'''
题目：给定一个二叉树，返回它的中序遍历。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class InorderTraversal():
    # 递归函数定义，返回以root为根结点的中序遍历的数组
    def medianTraversal(self, root:TreeNode):
        # 终止条件
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [root.val]
        else:
            # 递归的等价关系
            # 返回左子节点的中序遍历
            nums = self.medianTraversal(root.left)
            # 加入当前的根结点
            nums.append(root.val)
            # 加入右子节点的中序遍历
            nums.extend(self.medianTraversal(root.right))
            return nums
    def inorderTraversal(self, root:TreeNode):
        res = self.medianTraversal(root)
        return res

