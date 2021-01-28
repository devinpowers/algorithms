""" Project Using a Double Ended Queue"""




class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None
        
    def __repr__(self):
        """ Returns a rep of the data from the Node"""
        return self.data
    

class Deque:
    """ Represents a Double-Ended Queue"""
    
    def __init_(self):
        """Intializrs an Deque"""
        
        self.head = None
        self.tail = None
        self.length = 0
    
    def length(self):
        """Returns the length (number of Elements in the Deque"""
        
        return self.length
    
    def peek_front(self):
        """Returns, but doesnt remove the first element in the Deque"""
        
    
    def peek_back(self):
        pass
    
    def push_front(self, element):
        """
        Inserts an element to the Front
        of the Deque
        Parameter element: The Element to be Inserted
        """
        
        #1. Create a new node with the Element passed in!
        
        new_node = Node(element)
        #2. check if the Deque is Empty, if it is we will set head and tail to the node
        #3. If the Deque is not Empty, we will insert the new node where the head is
        
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.head.prev_node = new_node
            new_node.next_node = self.head()
            self.head = new_node
            
        self.length += 1
            
            
        
        
        
        
   
    
    def push_back(self, element):
        
        """
        Inserts an element to the Back
        of the Deque
        Parameter element: The Element to be Inserted
        """
        pass

    
    def pop_front(self):
        pass
    
    def pop_back(self):
        pass
    
    def clear(self):
        pass
    
    def __iter__(self):
        """Iterates over the Deque from front to back and returns an Iterator!"""
        pass
    
    def extend(self, other):
        pass
    
   
    
    def is_empty(self):
        pass
    
    def __repr__(self):
        pass
    
            
    