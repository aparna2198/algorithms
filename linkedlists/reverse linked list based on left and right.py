# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 12:47:30 2022

@author: APARNA
"""


class ListNode:
    def __init__(self, val=0, Next=None):
        self.val = val
        self.next = Next

    def print_linkedlist(self):
        head = self
        while head:
            print(head.val, "-->", end="\t")
            head = head.next
        print("Null")

    def reverse_list(self, left, right):
        head = self
        dummy = ListNode(Next = head)
        cur = head
        prevnode = dummy

        for i in range(left-1):
            prevnode, cur = cur, cur.next

        prev = None

        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        prevnode.next.next = cur
        prevnode.next = prev

        return dummy.next


ll2 = ListNode(4)
ll3 = ListNode(98)
ll4 = ListNode(100)
ll5 = ListNode(101)
ll6 = ListNode(33)
ll7 = ListNode(64,None)

ll2.next = ll3
ll3.next = ll4
ll4.next = ll5
ll5.next = ll6
ll6.next = ll7
ll2.print_linkedlist()

reversed_list = ll2.reverse_list(1, 3)
reversed_list.print_linkedlist()
