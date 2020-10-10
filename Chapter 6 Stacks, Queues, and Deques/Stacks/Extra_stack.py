
'''Extra Stack'''


class Stack():
    
    def __init__(self):
        self.items = []

    def push(self, item):
        '''Pushes element on the stack'''
        self.items.append(item)				

    def pop(self):
        '''Remove element from the top of the stack'''
        return self.items.pop()
    
    def is_empty(self):
        '''Check if Stack is empty'''
        return self.items == []
    
    def peek(self):
        '''Peek the top element on the stack'''
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        '''Return Stack list'''
        return self.items
    
    def __len__(self):
        return len(self.items)
    

s = Stack()
s.push("A")
s.push("B")
s.push('C')
s.push('D')
print('What did we pop?:',s.pop())

print(s.get_stack())

