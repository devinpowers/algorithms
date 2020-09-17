'''more practice with queue'''


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 
    

Q = Queue()


Q.enqueue(53)


Q.enqueue(43)


Q.enqueue(69)


Q.enqueue(70)


Q.enqueue(80)


Q.enqueue(5)

print(Q.dequeue())

print(Q.dequeue())
print(Q.dequeue())

print(Q.size())



