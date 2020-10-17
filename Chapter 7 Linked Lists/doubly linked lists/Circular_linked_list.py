
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    
    def __init__(self):
        
        self.head = None
        
    def append(self, data):
        
        if not self.head:  
            
            self.head = Node(data)
            self.head.next = self.head    
        
        else:
            new_node = Node(data)
            
            current = self.head
            
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            
            new_node.next = self.head
    
    
    def print_list(self):
        
        current = self.head
        
        while self.head:
            
            print(current.data)
            
            current = current.next
            
            if current == self.head:  
                break
        
             
    
    def prepend(self,data):
        
        new_node = Node(data)
        
        current = self.head
        
        new_node.next = self.head
        
        if not self.head:
            
            new_node.next = new_node
            
        else:
            
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
        
        self.head = new_node
    
  
    
cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.prepend('')
cllist.append("C")
cllist.append("D")

cllist.prepend("W")


cllist.print_list()

