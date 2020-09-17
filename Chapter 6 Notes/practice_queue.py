
# empty Querue
A = []

# length of Queue

N = len(A)

front = A[1]
rear = A[1]
clear


def Is_Empty():
    
    '''Checking if Queue is Empty'''
    if front == -1 and rear == -1:
        return True
    else:
        return False
    

def Enqueue(x):
    
    if (rear +1) % N == front:
        
        return
    
    elif Is_Empty():
        
        front,rear = 0
    else:
        rear = (rear+1)% N
    
    A[rear] = x
    
    

def Dequeue():
    
    if Is_Empty():
        return
    
    elif front == rear:
        front,rear = A[-1]
        
    else:
        front = (front + 1)% N




def front():
    '''Returning the value at the fronof the Queue'''
    
    return A[front]
    

Enqueue(4)