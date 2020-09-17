#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/6 10:36 下午
# @Author : xiongtao
# @File : 938_RangeSumBST.py 
# @Title : 938. 二叉搜索树的范围和

'''
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
二叉搜索树保证具有唯一的值。

输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉搜索树又称二叉排序树，左子树的值都小于根结点，右子树的值都大于根节点
class RangeSumBST:
    # 返回在值在L与R之间的数之和
    def rangeSumBST(self, root: TreeNode, L: int, R: int):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            if root.val >= L and root.val <= R:
                return root.val
        # 比较根结点的值与L、R
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return self.rangeSumBST(root.left, L, root.val) + self.rangeSumBST(root.right, root.val, R) + root.val