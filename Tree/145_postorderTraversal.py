#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/16 11:29 下午
# @Author : xiongtao
# @File : 145_postorderTraversal.py

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class PostorderTraversal():
    # 返回以root为根结点的后序遍历
    def postorderTraversal(self, root:TreeNode):
        if root==None:
            return None
        elif root.left==None and root.right==None:
            return [root.val]
        else:
            nums = self.postorderTraversal(root.left)
            nums.extend(self.postorderTraversal(root.right))
            nums.append(root.val)
            return nums