#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/8 11:46 下午
# @Author : xiongtao
# @File : 面试题 17.12_BiNode.py 
# @Title : 面试题 17.12. BiNode

'''
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。

输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BiNode:
    # 返回当前子树的单向链表的表头，中序遍历
    def biNode(self, root:TreeNode):
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root

        # 初始化左右子树的头节点
        left_root = None
        right_root = None

        # 遍历左子树，返回左子树变换后的单向链表的表头
        if root.left != None:
            left_root = self.biNode(root.left)
        # 如果左子树的表头为None，那就以当前的根结点为表头
        if left_root == None:
            left_root = root
        else:
            # 找到左子树最后一个节点
            left_last_Node = left_root
            while left_last_Node.right != None:
                left_last_Node = left_last_Node.right
            # 将左子树的最后一个节点指向根结点
            left_last_Node.right = root
            # 同时注意要将根结点的左子节点置空，不然会陷入死循环
            root.left = None
        # 找到右子树的表头
        if root.right != None:
            right_root = self.biNode(root.right)
        root.right = right_root
        return left_root

