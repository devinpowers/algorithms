

class MinHeap:
    
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0
 
    def print_(self):

        return self.heap_list
    
    def sift_up(self, i):
      
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2
 
    def insert(self, k):
     
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)
 
    
 
    def sift_down(self, i):
        
        # if the current node has at least one child
        
        print('Index:',i)
        
        while (i * 2) <= self.current_size:
            
            # Get the index of the min child of the current node
            miniumum_child = self.min_child(i)
            
            # Swap the values of the current element is greater than its min child
            
            if self.heap_list[i] > self.heap_list[miniumum_child]:
                
                self.heap_list[i], self.heap_list[miniumum_child] = self.heap_list[miniumum_child], self.heap_list[i]
            i = miniumum_child
 
    def min_child(self, i):
        
        # If the current node has only one child, return the index of the unique child
        
        if (i * 2)+1 > self.current_size:
            
            return i * 2
        
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
            
            
 
    def delete_min(self):
        
        # Equal to 1 since the heap list was initialized with a value
        
        if len(self.heap_list) == 1:
            return 'Empty heap'
 
        # Get root of the heap (The min value of the heap)
        
        root = self.heap_list[1]
 
        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]
        
        print("Current Array looks like", self.heap_list)
        
 
        # Pop the last value since a copy was set on the root
        *self.heap_list, _ = self.heap_list
        
        print("Array looks like this now:", self.heap_list)
 
        # Decrease the size of the heap
        self.current_size -= 1
 
        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)
        
 
        # Return the min value of the heap
        return root
"""
Driver program
"""
# Same tree as above example.
my_heap = MinHeap()
my_heap.insert(10)
my_heap.insert(30)
my_heap.insert(20)
my_heap.insert(35)
my_heap.insert(40)
my_heap.insert(32)
my_heap.insert(25)
print("Before Deletion")

print(my_heap.print_())

print("\nAfter Deletion")
print(my_heap.delete_min()) # removing min node i.e 5 
print(my_heap.print_())