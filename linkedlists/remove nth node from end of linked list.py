# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 20:20:27 2022

@author: APARNA
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def add_node_last(self,val):
        if self.head:
            head = self.head
            while head:
                if not head.next:
                    head.next = Node(val)
                    break
                head = head.next
            
            
        else:
            self.head = Node(val)
    
    def print_linkedlist(self):
        head = self.head
        while(head):
            print(head.val, end = "-->\t")
            head = head.next
        
        print("None")
    
    def delete_end_nth_node(self, n):
        head = self.head
        dummy = LinkedList()
        dummy.next = head
        left = dummy
        right = head
        
        while n>0:
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

            


ll2 = LinkedList()
ll2.add_node_last(4)
ll2.add_node_last(33)
ll2.add_node_last(64)
ll2.add_node_last(98)
ll2.add_node_last(100) 
ll2.add_node_last(101) 
ll2.print_linkedlist()
ll2.delete_end_nth_node(1)
ll2.print_linkedlist()

            