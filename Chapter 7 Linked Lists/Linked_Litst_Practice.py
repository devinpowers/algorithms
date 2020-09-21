#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:37:19 2020

Linked Lists
https://www.geeksforgeeks.org/linked-list-set-1-introduction/

@author: devinpowers
"""

# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
        

# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    llist.head = Node(1) 
    
    second = Node(2) 
    
    third = Node(3) 
        
    
    