# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 02:04:34 2022

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
        
   
        
    def remove_data(self,data):
        dummy = LinkedList()
        dummy.next = self.head
        
        prev,curr = dummy, self.head
        
        while curr:
            nxt = curr.next
            if curr.data == data:
                prev.next = nxt
            else:
                prev = curr
            curr = curr.next
        
        self.head = dummy.next
        
        
        
                
ll1 = LinkedList()

ll1.add_node_last(32)
ll1.add_node_last(65)
ll1.add_node_last(99)
ll1.add_node_last(4)
ll1.add_node_last(99)
ll1.add_node_last(64)
ll1.add_node_last(98) 
ll1.print_linkedlist() 
ll1.remove_data(99)
ll1.print_linkedlist()