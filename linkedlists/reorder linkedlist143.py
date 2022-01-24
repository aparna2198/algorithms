# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 01:22:11 2022

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
        
   
        
    # logic is 
    # 1)bisect into two halves
    # 2) get two pointer 
    # 3)go nuts while appending one after the other 
        
    def reorder_linkedlist(self):
        head = self.head
        slow, fast = head, head.next
        
        # to bisect the linked list into two we need midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first,second = head, prev
        while second:
            temp1, temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2
        
        self.head = head
                
ll1 = LinkedList()

ll1.add_node_last(32)
ll1.add_node_last(65)
ll1.add_node_last(99)
ll1.add_node_last(4)
ll1.add_node_last(33)
ll1.add_node_last(64)
ll1.add_node_last(98) 
ll1.print_linkedlist() 
ll1.reorder_linkedlist()
ll1.print_linkedlist()
