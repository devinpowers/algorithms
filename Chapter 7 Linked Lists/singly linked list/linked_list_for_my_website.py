

class Node:
    
    def __init__ (self,data):
        self.data = data
        self.next = None

class linkedList():
    
    def __init__(self):
        self.head = None
        
    def print_list(self):
        
        current_node = self.head
        
        while current_node:
            
            print(current_node.data)
            current_node = current_node.next
    
    
    def append(self, data):
        
        new_node = Node(data)
        
        if self.head is None:
        
            self.head = new_node
            
            return
        
        last_node = self.head
        
        while last_node.next:
            # loop thru linked list until last_node.next is pointing to null
            last_node = last_node.next
            
        # after it exits the loop, we append new node:
            
        last_node.next = new_node
    
    def prepend(self,data):
        
        new_node = Node(data)
        
        new_node.next = self.head 
        
        self.head = new_node
    
    
    def delete_node(self, key):
        
        current_node = self.head
        
        if current_node and current_node.data == key:
            
            self.head = current_node.next
            
            current_node = None
            
            return
    
        previous = None
        
        while current_node and current_node.data != key:
            
            previous = current_node
            
            current_node = current_node.next
            
        
        if current_node is None:
            return
        
        previous.next = current_node.next
        
        current_node = None
    
    def delete_node_at_pos(self, position):
        

        current_node = self.head

        if position == 0:
            
            self.head = current_node.next
            
            current_node = None
            
            return


        previous = None
        
        count = 0
        
        while current_node and count != position:
            
            previous = current_node 
            
            current_node = current_node.next
            
            count += 1

        if current_node is None:
            
            return 

        previous.next = current_node.next
        
        current_node = None
        
    
    def length_iterative(self):
        
        count = 0
        
        current_node = self.head
        
        while current_node:
            count += 1
            current_node = current_node.next
        
        return count
    

    
    def print_helper(self, node, name):
        
        if node is None:
            print(name + ": None")
        
        else:
            print(name + ":" + node.data)
            
    
    def reverse_iterative(self):
        
        previous = None
        
        current_node = self.head
        
        while current_node:
            
            
            next_node = current_node.next
    
            current_node.next = previous
            
            self.print_helper(previous, "Previous")
            self.print_helper(current_node, "Current Node")
            self.print_helper(next_node, "Next Node")
            print("\n")
            
            previous = current_node
            
            current_node = next_node
            
        self.head = previous
            
            
            
     
        
        

    

ll = linkedList()


ll.append('A')
ll.append('B')
ll.append('C')
ll.append('D')
ll.append('E')


ll.print_list()

print('After Reverse')
print('\n')

ll.reverse_iterative()
ll.print_list()


