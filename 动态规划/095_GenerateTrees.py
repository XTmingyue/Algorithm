#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/10/9 4:53 下午
# @Author : xiongtao
# @File : 095_GenerateTrees.py 
# @Title : 95. 不同的二叉搜索树 II

'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
示例：
输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Sloution:
    '''
    题解：递归
    1 ... n中任意一个节点都可以作为根结点。
    因此，可以遍历每个节点，将其左侧的数作为左子节点中的数，右侧的数作为右子节点中的数。
    对于左右子节点也进行相同的操作。
    '''
    # 返回[start, end]之间所有可行的二叉搜索树
    def generateTreesSub(self, start, end):
        if start > end:
            return [None]
        res = []
        for i in range(start, end + 1):
            left_Trees = self.generateTreesSub(start, i - 1)
            right_Trees = self.generateTreesSub(i + 1, end)
            for left_Tree in left_Trees:
                for right_Tree in right_Trees:
                    root = TreeNode(i)
                    root.left = left_Tree
                    root.right = right_Tree
                    res.append(root)
        return res
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.generateTreesSub(1, n)





