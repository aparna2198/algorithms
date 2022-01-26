# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 23:41:50 2022

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
        
    @staticmethod
    def add_twonumbers(l1,l2):
        new_list = LinkedList()
        dummy = LinkedList()
        dummy.add_node_last(0)
        
        
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.data if l1 else 0
            v2 = l2.data if l2 else 0
            
            val = v1 + v2 + carry
            carry = val //10
            val = val%10
            
            new_list.add_node_last(val)
            
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return new_list
            
        
ll1 = LinkedList()

ll1.add_node_last(9)
ll1.add_node_last(9)
ll1.add_node_last(9) 
ll1.add_node_last(9)
ll1.add_node_last(9)
ll1.add_node_last(9)
ll1.add_node_last(9)
ll1.print_linkedlist() 


ll2 = LinkedList()
ll2.add_node_last(9)
ll2.add_node_last(9)
ll2.add_node_last(9)
ll2.add_node_last(9)
ll2.print_linkedlist()

ll3 = LinkedList.add_twonumbers(ll1.head,ll2.head)
ll3.print_linkedlist() 
