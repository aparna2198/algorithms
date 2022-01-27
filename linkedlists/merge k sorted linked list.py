# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 23:12:37 2022

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
    def merge(ll1,ll2):
        ll1head = ll1.head
        ll2head = ll2.head
        ll3 = LinkedList()
        if not ll1head:
            return ll2
        if not ll2head:
            return ll1
        
        while ll1head and ll2head:
            if ll1head.data<=ll2head.data:
                ll3.add_node_last(ll1head.data)
                ll1head = ll1head.next
            else:
                ll3.add_node_last(ll2head.data)
                ll2head = ll2head.next
        
        while ll1head:
            ll3.add_node_last(ll1head.data)
            ll1head = ll1head.next
        
        while ll2head:
            ll3.add_node_last(ll2head.data)
            ll2head = ll2head.next
        
        return ll3
    
    @staticmethod
    def merge_klists(lists):
        
        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            merged_lists = []
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else LinkedList()
                
                merged_lists.append(LinkedList.merge(l1,l2))
            lists = merged_lists
        
        return lists[0]
                
        
        
    
ll1 = LinkedList()
ll1.add_node_last(32)
ll1.add_node_last(65)
ll1.add_node_last(99) 
ll1.print_linkedlist() 


ll2 = LinkedList()
ll2.add_node_last(4)
ll2.add_node_last(33)
ll2.add_node_last(64)
ll2.add_node_last(98)
ll2.add_node_last(100) 
ll2.print_linkedlist()


ll3 = LinkedList()
ll3.add_node_last(4)
ll3.add_node_last(9)
ll3.add_node_last(81)
ll3.add_node_last(97)
ll3.add_node_last(105) 
ll3.print_linkedlist()

merged_list = LinkedList.merge_klists([ll1,ll2,ll3])

merged_list.print_linkedlist()
