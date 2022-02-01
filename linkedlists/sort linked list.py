# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 01:33:21 2022

@author: APARNA
"""

class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
    
    def print_linkedlist(self):
        head = self
        while head:
            print(head.val,"-->",end = "\t")
            head = head.next
        print("Null")
    
class Solution:
    def sortList(self, head):
        
        if not head or not head.next:
            return head
        
        left = head
        right = self.getmid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left,right)
    
    def getmid(self, head):
        
        if not head:
            return head
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def merge(self, left,right):
        
        dummy = ListNode()
        curr = dummy
        if not left:return right
        if not right: return left
        while left and right:
            if left.val < right.val:
                curr.next = ListNode(left.val)
                left = left.next
            else:
                curr.next = ListNode(right.val)
                right = right.next
            
            curr  = curr.next
        
        if left:
            curr.next = left
        if right:
            curr.next = right
        
        return dummy.next
                
            
        
ll1 = ListNode(10)
ll2 = ListNode(99, next = ll1)
ll3 = ListNode(91,next = ll2)
ll4 = ListNode(1,next = ll3)
ll3 = ListNode(12, next = ll4)

ll3.print_linkedlist()
sol_obj =Solution()
sorted_list = sol_obj.sortList(ll3)
sorted_list.print_linkedlist()

