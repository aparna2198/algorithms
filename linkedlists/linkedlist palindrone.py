# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 20:41:01 2022

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
        
    def is_palindrone(self):
        slow, fast = self.head,self.head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first,second = self.head, slow.next
        
#        reverse second half of the list
        prev=slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp
        
        while first and prev:
            
            if first.data != prev.data:
                return False
            first = first.next
            prev = prev.next
        return True
    
                
ll1 = LinkedList()

ll1.add_node_last(32)
ll1.add_node_last(65)
ll1.add_node_last(99)
ll1.add_node_last(99)
ll1.add_node_last(65)
ll1.add_node_last(32)
# ll1.add_node_last(32) 
ll1.is_palindrone() 