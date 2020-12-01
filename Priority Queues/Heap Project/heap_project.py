


class Heap:

    """
    A heap-based priority queue
    """

    def __init__(self, comp):

        """
        Constructor
        :param comp: A comparison function determining the priority of the
        included elements
        
        includes size and a list (Heao)
        """

        self.comp = comp
        # Added Members

        self.h = []
        self.size = 0

    def __len__(self):

        """
        Length of heap
        """
        
        
        return self.size 
    def __bool__(self):
        

        """
        Checks if this heap contains items
        :return: True if the heap is non-empty
        """

        return not self.is_empty()

    def is_empty(self):

        """
        Checks if this heap is empty
        :return: True if the heap is empty
        """

        return len(self) == 0

    def __repr__(self):

        """
        A string representation of this heap
        :return:
        """

        return 'Heap([{0}])'.format(','.join(str(item) for item in self))

    

    def peek(self):
        
        "Returns the Min value/ Root Value"
        
        if self.is_empty():
            
            raise IndexError
        
        return self.h[0] # index 0
    
    def insert(self, item):
        """Inserts a value into the heap"""
        
        self.size += 1
        
        self.h.append(item)
        
        
        i = len(self) - 1
        
        while i > 0 and self.comp(item, self.h[parent(i)]):
            
            self.h[i] = self.h[parent(i)]

            i = parent(i)
            
        self.h[i] = item
        
    
    
    
    def clear(self):
        
        """Resets the heap to be empty"""
        
        self.h = []
        self.size = 0
        
        
    def heapify(self, key):

        """
        Heapifies current heap starting at key in place
        :param key: index to start at
        :return: None
        """

        left = 2 * key + 1
        right = 2 * key + 2

        if left < len(self) and self.comp(self.h[left], self.h[key]):

            small = left

        else:

            small = key

        if right < len(self) and self.comp(self.h[right], self.h[small]):

            small = right

        if small != key:

            self.h[key], self.h[small] = self.h[small], self.h[key]

            self.heapify(small)
      
        
            
        kava
        

    