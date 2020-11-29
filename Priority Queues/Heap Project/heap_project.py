


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
        
        i = len(self)