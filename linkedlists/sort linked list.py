# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 22:50:38 2022

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
    
    @staticmethod
    def node_traverse(head):
        while(head):
            print(head.val, end = "-->\t")
            head = head.next
        
        print("None")
    
    def sort_linklist(self,head):
        if not head or not head.next:
            return head
        
        left = head
        right = self.getmid(head)
        
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sort_linklist(left)
        right = self.sort_linklist(right)
        
        return self.merge(left, right)
    
    def getmid(self,head):
         
        left = head
        right = head.next
        while right and right.next:
            right = right.next
            left = left.next
        return left
            
    def merge(self,left, right):
        
        
        
        curr = dummy  = LinkedList()
         
        if not left:
            return right
        if not right: 
            print("in 66",type(left.next))
            return left
        while left and right:
            if left.val < right.val:
                curr.add_node_last(left.val)
                left = left.next
            else:
                curr.add_node_last(right.val)
                right = right.next
            
            
        while left:
            curr.add_node_last(left.val)
            left = left.next
        if right:
            curr.add_node_last(right.val)
            right = right.next
        
        return dummy.head.next
        
        

ll2 = LinkedList()
ll2.add_node_last(101)
ll2.add_node_last(33)
ll2.add_node_last(98)
ll2.add_node_last(64)
ll2.add_node_last(4)
ll2.add_node_last(100) 
ll2.add_node_last(110) 
ll2.print_linkedlist()
new_list  = ll2.sort_linklist(ll2.head)
LinkedList.node_traverse(new_list)
