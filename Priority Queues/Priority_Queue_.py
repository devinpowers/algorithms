
class Node:
    
    def __init__(self, item, priority):
        
        self.item = item
        self.next = None
        self.priority = priority

class PriorityQueue:
    
    def __init__(self):
        
        self.front = None
        self.rear = None
        
    def isEmpty(self):
        
        return self.front == None
    
    def enqueue(self, item, priority):
        
        newNode = Node(item, priority)
        
        if not self.rear:
            self.front = newNode
            self.rear = newNode
            return
        
        if self.front.priority < newNode.priority:
            
            newNode.next = self.front
            
            self.fron = newNode
            
            return
        previous = None
        current = self.front
        
        while current and newNode.priority < current.priority:
            previous = current
            current = current.next
            
        if current:
            
            previous.next = newNode
            
            newNode.next = current
        
        else:
            self.rear.next = newNode
            self.rear = newNode
        
        
        
    def dequeue(self):
        
        if self.isEmpty():
            print("The Queue is empty")
            return
        
        temp = self.front 
        self.front = self.front.next
        if self.front == None:
            self.rear = None
            
        return temp.item
    
q = PriorityQueue()

q.enqueue('Devin', 2)
q.enqueue('Kobe', 2)
q.enqueue('Lebron', 10)
q.enqueue('Paul', 3)
q.enqueue('Jordan', 12)


