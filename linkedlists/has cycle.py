# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 22:51:30 2022

@author: APARNA
"""

class ListNode:
    def __init__(self,val = 0,Next = None):
        self.val = val
        self.next = Next
    
    def print_linkedlist(self):
       head = self
       while head:
           print(head.val,"-->",end = "\t")
           head = head.next
       print("Null")
      
    def has_cycle(self):
        dummy  = ListNode(Next = self)
        slow = dummy
        fast = self
        head = self
        while fast and fast.next and head:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next 
            head = head.next            
        return False


ll4 = ListNode(4)
ll0 = ListNode(0)
ll2 = ListNode(2)       
ll3 = ListNode(3)

ll3.next = ll2
ll2.next = ll0
ll0.next = ll4
ll4.next = ll2
# ll4.next = None


print(ll4.has_cycle())
