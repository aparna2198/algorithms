# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 23:58:15 2022

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
    
    def delete_middle_node(self):
        
        if not self.head or not self.head.next:
            return None
        dummy = LinkedList()
        dummy.next = self.head
        slow =  dummy
        
        fast =  self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        slow.next = slow.next.next
        # if fast and not fast.next:
        #     slow.next = slow.next.next
        # else:
        #     prev.next = slow.next
        
        
        
ll2 = LinkedList()
ll2.add_node_last(4)
ll2.add_node_last(33)
ll2.add_node_last(64)
ll2.add_node_last(98)
ll2.add_node_last(100) 
# ll2.add_node_last(101) 
ll2.print_linkedlist()
ll2.delete_middle_node()
ll2.print_linkedlist()