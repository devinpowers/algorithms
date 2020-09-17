'''More Stack Practice'''

class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)
    

S= Stack()

S.push(3)
S.push(5)
S.push(6)
S.push(10)
S.push(12)


print(S.size())

print(S.pop())
