# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 00:28:46 2022

@author: APARNA
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_node_last(self,data):
        head = self.head
        if head:
            while head:
                if not head.next:
                    head.next = Node(data)
                    break
                head = head.next
        else:
            self.head = Node(data)
    
    def add_node_first(self,data):
        head = self.head
        if head:
            new_node = Node(data)
            new_node.next = head
            self.head = new_node
        else:
            self.head = Node(data)
    
    def print_linkedlist(self):
        head = self.head
        while head:
            print(head.data,"-->",end = "\t")
            head = head.next
        print("Null")
    
    def swap_nodes(self):
        head = self.head
        dummy = LinkedList()
       
        prev, cur = dummy, head
        
        while cur and cur.next:
            third = cur.next.next
            second = cur.next
            
            second.next = cur
            cur.next = third
            prev.next = second
            
            prev = cur
            cur = cur.next
        
        print(type(dummy.next))
        self.head  = dummy.next
    
ll2 = LinkedList()
ll2.add_node_last(4)
ll2.add_node_last(33)
ll2.add_node_last(64)
ll2.add_node_last(98)
ll2.add_node_last(100) 
ll2.add_node_last(101) 
ll2.print_linkedlist()

ll2.swap_nodes()
ll2.print_linkedlist()
