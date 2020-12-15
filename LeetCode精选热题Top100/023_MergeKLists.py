#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/12/1 8:28 上午
# @Author : xiongtao
# @File : 023_MergeKLists.py 
# @Title : 23. 合并K个升序链表

'''
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    题解：递归 -- 超时
    函数返回链表数组中的升序链接的链表表头
    '''
    # 移除空链表
    def remove_None(self, lists):
        res = []
        for val in lists:
            if val != None:
                res.append(val)
        return res

    def mergeKLists(self, lists):
        lists = self.remove_None(lists)
        head = None
        if len(lists) == 0:
            return head
        if len(lists) == 1:
            head = lists[0]
            return head
        # 记录当前最小的节点下标
        curr_node_index = -1
        for i in range(len(lists)):
            if curr_node_index == -1:
                curr_node_index = i
            elif lists[curr_node_index].val > lists[i].val:
                curr_node_index = i
        if curr_node_index == -1:
            return None
        head = lists[curr_node_index]
        if lists[curr_node_index].next == None:
            lists.pop(curr_node_index)
        else:
            lists[curr_node_index] = lists[curr_node_index].next
        head.next = self.mergeKLists(lists)
        return head

    '''
    题解：朴素法-保存ans，每次取列表中的一个合并到ans中 -- AC
    '''
    # 合并两个链表
    def merge_list(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head = ListNode()
        curr_node = head
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next
        if list1 == None:
            curr_node.next = list2
        if list2 == None:
            curr_node.next = list1
        return head.next

    def mergeKLists_2(self, lists):
        if len(lists) == 0:
            return None
        head = lists[0]
        for i in range(1, len(lists)):
            head = self.merge_list(head, lists[i])
        return head

    '''
    题解：两两合并
    '''
    def mergeKLists_3(self, lists):
        if len(lists) == 0:
            return None
        return self.merge_range(lists, 0, len(lists)-1)

    def merge_range(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = self.merge_range(lists, left, mid)
        l2 = self.merge_range(lists, mid + 1, right)
        return self.merge_list(l1, l2)



if __name__ == '__main__':
    list_1 = ListNode(1)
    list_1.next = ListNode(4)
    list_1.next.next = ListNode(5)

    list_2 = ListNode(1)
    list_2.next = ListNode(3)
    list_2.next.next = ListNode(4)

    list_3 = ListNode(2)
    list_3.next = ListNode(6)

    # lists = [list_1, list_2, list_3]
    class_S = Solution()
    lists = [None, [ListNode(1)]]
    print(class_S.mergeKLists_3(lists))