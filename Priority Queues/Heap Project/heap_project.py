


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
        
        

    def __iter__(self):
        """
        An iterator for this heap
        :return: An iterator
        """
        return iter(self.data)

    # Supplied methods

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





    # Added methods
    def sift_up(self, i):
        """
        Move elements in the heap until they meet criteria
        :param i: index of element
        """
        p = parent(i)
        # Only swap if not at first element and need to swap
        if i > 0 and self.comp(self.data[i], self.data[p]):
            # Swap
            self.swap(i, p)
            self.sift_up(p)

    def swap(self, i, j):
        """
        Swap two elements in heap
        :param i: index of first elem
        :param j: index of second elem
        """
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def sift_down(self, i):
        """
        Move elements in heap until they meet criteria
        :param i: index
        """
        if self.has_left(i):
            l = left(i)
            smallest_child = l
            # Check if right child is smaller
            if self.has_right(i):
                r = right(i)
                if self.comp(self.data[r], self.data[l]):
                    smallest_child = r
            # Check if swap smallest child
            if self.comp(self.data[smallest_child], self.data[i]):
                self.swap(i, smallest_child)
                self.sift_down(smallest_child)

    def has_left(self, i):
        """
        check if item has left child
        :param i: item to check
        :return: True or False
        """
        return left(i) < len(self.data)

    def has_right(self, i):
        """
        check if item has right child
        :param i: item to check
        :return: True or False
        """
        return right(i) < len(self.data)



            
        
        


def find_median(seq):
    """
    Finds the median (middle) item of the given sequence.
    Ties are broken arbitrarily.
    Strategy - extend seq to each heap then do n//2+1 extractions to determine the median
    :param seq: an iterable sequence
    :return: the median element
    """
    # If seq is empty
    if not seq:
        raise IndexError

    # Extend seq to each heap. Affected by lambda
    min_heap = Heap(lambda a, b: a < b)
    min_heap.extend(seq)
    max_heap = Heap(lambda a, b: a > b)
    max_heap.extend(seq)

    # Doing n//2+1 returns the median
    for _ in range(len(max_heap)//2+1):
        max_mid = max_heap.extract()
    for _ in range(len(min_heap)//2+1):
        min_mid = min_heap.extract()

    # If seq is even, can return either median item
    if len(seq)%2 == 1:
        return max_mid
    return min_mid


def parent(i):
    """
    Return the parent index of given index
    :param i: item to get parent of
    :return: index of parent
    """
    return (i - 1) // 2


def left(i):
    """
    Return the left child index of given index
    :param i: item to get left child of
    :return: index of left child
    """
    return 2 * i + 1


def right(i):
    """
    Return the right child index of given index
    :param i: item to get right child of
    :return: index of right child
    """
    return 2 * i + 2


def main(filename):
    with open(filename, 'r') as reader:
        text = [line.strip() for line in reader]
        median = find_median(text)
        print('Median:', median)


if __name__ == '__main__':
    main('alphabet.txt')
