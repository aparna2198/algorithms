# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:03:40 2022

@author: APARNA
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_node(self,data):
        head = self.head
        if head:
            while head:
                if not head.next:
                    head.next = Node(data)
                    break
                head = head.next
        else:
            self.head = Node(data)
    
    def print_linkedlist(self):
        head = self.head
        while head:
            print(head.data,"-->",end = "\t")
            head = head.next
        print("Null")
        
    @staticmethod
    def merge(ll1head,ll2head):
        ll3 = LinkedList()
        if not ll1head:
            return ll2head
        if not ll2head:
            return ll1head
        
        while ll1head and ll2head:
            if ll1head.data<=ll2head.data:
                ll3.add_node(ll1head.data)
                ll1head = ll1head.next
            else:
                ll3.add_node(ll2head.data)
                ll2head = ll2head.next
        
        while ll1head:
            ll3.add_node(ll1head.data)
            ll1head = ll1head.next
        
        while ll2head:
            ll3.add_node(ll2head.data)
            ll2head = ll2head.next
        
        return ll3
                
                
        
ll1 = LinkedList()
ll1.add_node(32)
ll1.add_node(65)
ll1.add_node(99) 
ll1.print_linkedlist() 

ll2 = LinkedList()
ll2.add_node(4)
ll2.add_node(33)
ll2.add_node(64)
ll2.add_node(98)
ll2.add_node(100) 
ll2.print_linkedlist()

ll3 = LinkedList.merge(ll1.head,ll2.head)
ll3.print_linkedlist() 
