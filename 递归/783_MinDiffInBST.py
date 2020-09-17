#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/9/3 9:58 下午
# @Author : xiongtao
# @File : 783_MinDiffInBST.py 
# @Title : 783. 二叉搜索树节点最小距离

'''
给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MinDiffInBST:
    def findTop2Min(self, root:TreeNode, top_2_min):
        top_2_min.append(root.val)
        if root.left != None:
            self.findTop2Min(root.left, top_2_min)
        if root.right != None:
            self.findTop2Min(root.right, top_2_min)
    def minDiffInBST(self, root:TreeNode):
        top_2_min = []
        self.findTop2Min(root, top_2_min)
        top_2_min.sort()
        min_diff = top_2_min[1] - top_2_min[0]
        for i in range(2, len(top_2_min)):
            if top_2_min[i] - top_2_min[i-1] < min_diff:
                min_diff = top_2_min[i] - top_2_min[i-1]
        return min_diff

if __name__ == '__main__':
    class_minDiff = MinDiffInBST()
    root = TreeNode()
    print(class_minDiff.minDiffInBST(root))


