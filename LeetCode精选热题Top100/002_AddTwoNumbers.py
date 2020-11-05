#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/11/4 8:28 上午
# @Author : xiongtao
# @File : 002_AddTwoNumbers.py 
# @Title : 2. 两数相加

'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbers:
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        num = l1.val + l2.val - 10 if (l1.val + l2.val) >= 10 else l1.val + l2.val
        # 保存进位
        cum = 1 if (l1.val + l2.val) >= 10 else 0
        head = ListNode(num)
        l1 = l1.next
        l2 = l2.next
        res = head
        while l1 != None or l2 != None:
            if l1 == None:
                num = l2.val + cum - 10 if (l2.val + cum) >= 10 else l2.val + cum
                cum = 1 if (l2.val + cum) >= 10 else 0
                res.next = ListNode(num)
                l2 = l2.next
            elif l2 == None:
                num = l1.val + cum - 10 if (l1.val + cum) >= 10 else l1.val + cum
                cum = 1 if (l1.val + cum) >= 10 else 0
                res.next = ListNode(num)
                l1 = l1.next
            else:
                num = l1.val + l2.val + cum - 10 if (l1.val + l2.val + cum) >= 10 else l1.val + l2.val + cum
                cum = 1 if (l1.val + l2.val + cum) >= 10 else 0
                res.next = ListNode(num)
                l1 = l1.next
                l2 = l2.next
            res = res.next
        if cum == 1:
            res.next = ListNode(1)
        return head

