


class Heap:

    """
    A heap-based priority queue
    Items in the queue are ordered according to a comparison function
    """

    def __init__(self, comp):

        """
        Constructor
        :param comp: A comparison function determining the priority of the
        included elements
        """

        self.comp = comp
        # Added Members

        self.h = []
        self.size = 0

    def __len__(self):

        """
        Length of heap
        :return: length of heap
        """

        return self.size 