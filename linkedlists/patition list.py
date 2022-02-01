# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 01:56:01 2022

@author: APARNA
"""

class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.lastnode = None
    
    def add_node(self,data):
        if self.head:
            head = self.head
            while head:
                if not head.next:
                    head.next = Node(data)
                    self.lastnode = head.next
                    break
                head = head.next
            
        else:
            self.head = Node(data)
    
    def print_linkedlist(self):
        head = self.head
        while head:
            print(head.val,"-->",end = "\t")
            head = head.next
        print("Null")
    
    def partition(self,n):
        left =  LinkedList()
        right = LinkedList()
        ltail = left
        rtail = right
        head = self.head
        while head:
            if head.val < n:
                ltail.add_node(head.val)
                left = ltail.lastnode
            else:
                rtail.add_node(head.val)
                right = rtail.lastnode
            head = head.next
        
        
        ltail.lastnode.next = rtail.head
        rtail.lastnode = None
        
        return ltail        
        

ll2 = LinkedList()
ll2.add_node(4)
ll2.add_node(98)
ll2.add_node(100) 
ll2.add_node(101) 
ll2.add_node(33)
ll2.add_node(64)

ll2.print_linkedlist()
ll3 = ll2.partition(65)
ll3.print_linkedlist()
