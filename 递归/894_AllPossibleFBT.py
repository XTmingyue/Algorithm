#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/3 11:15 下午
# @Author : xiongtao
# @File : 894_AllPossibleFBT.py 
# @Title : 894. 所有可能的满二叉树

'''
满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。

答案中每个树的每个结点都必须有 node.val=0。

你可以按任何顺序返回树的最终列表。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 函数返回的是包含N个节点的所有满二叉树的列表
    def allPossibleFBT(self, N: int):
        if N == 1:
            return [TreeNode(0)]
        # 满二叉树的节点必须是偶数
        if N % 2 == 0:
            return []
        res = []
        # 左子树分配一个节点
        left_num = 1
        # 右子数分配剩余节点
        right_num = N - left_num - 1

        # 左右子树至少要有一个节点才能满足当前树是满二叉树
        while right_num > 0:
            # 左右子数也要是满二叉树，遍历所有可能的左右子树进行组合
            left_trees = self.allPossibleFBT(left_num)
            right_trees = self.allPossibleFBT(right_num)
            for i in range(0, len(left_trees)):
                for j in range(0, len(right_trees)):
                    root = TreeNode(0)
                    root.left = left_trees[i]
                    root.right = right_trees[j]
                    res.append(root)
            left_num += 2
            right_num = N - left_num - 1
        return res

if __name__ == '__main__':
    class_FBT = Solution()
    print(class_FBT.allPossibleFBT(7))
