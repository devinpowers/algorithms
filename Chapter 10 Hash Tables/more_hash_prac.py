
INITIAL_CAPACITY = 10


class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self)
    

class HashTabke:
    
    def __init_(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None]*self.capacity
        
    
    def hash(self, key):
        hash_sum = 0
        
        for index, c in enumerate(key):
            
            hash_sum += (index + len(key)) ** ord(c)
            
            hash_sum = hash_sum % self.capacity
        
        return hash_sum
    
    
        