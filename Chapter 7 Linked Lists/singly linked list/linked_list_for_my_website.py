

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
    
    def insertion_after_node(self, previous_node, data):
        
        if not previous_node:
            print("Previous node is not in the list")
            return
        
        new_node = Node(data)
        
        new_node.next = previous_node.next
        previous_node.next = new_node
    
    
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
        
        
    def merge_sorted(self, llist):
        
        p = self.head
        q = llist.head
        s = None
        
        if not p:
            return q
        
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            
            new_head = s
                    
        while p and q:
            
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            
            else:
                s.next = q
                s = q
                q = s.next
        
        if not p:
            s.next = q
        
        if not q:
            s.next = p
        
        return new_head
    


llist_1 = linkedList()
llist_2 = linkedList()


llist_1.append('1')
llist_1.append('5')
llist_1.append('7')
llist_1.append('9')
llist_1.append('10')

llist_2.append('2')
llist_2.append('3')
llist_2.append('4')
llist_2.append('6')
llist_2.append('8')

llist_1.merge_sorted(llist_2)
llist_1.print_list()


