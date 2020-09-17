#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/6 10:58 下午
# @Author : xiongtao
# @File : 剑指0ffer_BuildTree.py 
# @Title : 剑指 Offer 07. 重建二叉树

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

    3
   / \
  9  20
    /  \
   15   7
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class RebulidTree:
    # 返回的是以preorder, inorder构成的树的根结点
    def bulidTree(self, preorder, inorder):
        if len(inorder) <= 0 or len(preorder) <= 0:
            return None
        # 以前序数组的第一个值为根结点
        root = TreeNode(preorder[0])

        # 以根结点对中序遍历进行拆分，拆分出左子树和右子树
        split_index = 0
        for i in range(0, len(inorder)):
            if inorder[i] == preorder[0]:
                split_index = i
                break
        left_inorder = []
        right_inorder = []
        if i > 0:
            left_inorder = inorder[0:i]
        if i < len(inorder) - 1:
            right_inorder = inorder[i+1:]

        # 前序遍历第一个元素是根结点，剩下的先是左子树的节点，在是右子树的节点
        left_preorder = []
        right_preorder = []
        if len(left_inorder) > 0:
            left_preorder = preorder[1:len(left_inorder)+1]
        if len(right_inorder) > 0:
            right_preorder = preorder[len(left_inorder)+1:]

        root.left = self.bulidTree(left_preorder, left_inorder)
        root.right = self.bulidTree(right_preorder, right_inorder)
        return root


