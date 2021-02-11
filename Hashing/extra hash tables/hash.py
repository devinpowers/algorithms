
class HashNode:
    """
    Represents a HashNode!
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "HashNode({self.key}, {self.value})"  # f"HashNode({self.key}, {self.value})"



class HashTable:
    """
    Hash table class, utilizes double hashing for conflicts
    """

    def __init__(self, capacity=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None]*capacity

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        pass

    def hash_function(self, x):
        """
        ---DO NOT EDIT---

        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.capacity

    def insert(self, key, value):
        """
        Inserts a node with the provided key and value into the Hash Table. If a node with
        the same key is already present, update its value to the value parameter. Doesn't allow
        insertion of an empty key.
        :param key: Key to insert into the Hash Table
        :param value: Value to insert into the Hash Table
        :return: No return
        """
        if key is None or len(key) == 0:  # Doesnt't allow insertion of empty string
            return

        # If a HashNode with the same key is already present, reassigns the value to the new value
        counter = 0
        while counter < self.capacity:  # If node with same key is already present, reassigns value
            temp_node = self.table[counter]
            if temp_node is not None and temp_node.key == key:
                self.table[counter].value = value
                return
            counter += 1

        bucket = self.hash_function(key)
        if self.table[bucket] is None:
            self.table[bucket] = HashNode(key, value)
        else:
            index = self.quadratic_probe(key)
            temp = self.table[index]
            if temp is None:
                self.table[index] = HashNode(key, value)

        self.size += 1
        load = float(self.size) / float(self.capacity)
        if load > 0.75:
            self.grow()

    def quadratic_probe(self, key):
        """
        Runs the quadratic hashing procedure to get an empty position to insert node into
        (or the position of a matching key).
        :param key: Key of the node to be inserted into the table
        :return: Returns the next available index of where the node should be inserted or
        returns the index of key if key is already in the Hash Table.
        """
        index = self.hash_function(key)

        if self.table[index] is None:
            return index

        counter = 1

        while 1:
            old_position = index
            index = (old_position + (counter * counter)) % self.capacity
            if self.table[index] is None:
                return index
            else:
                counter += 1

    def find(self, key):
        """
        Searches for a given key in the Hash Table. If found, return the node with the given key.
        Otherwise, return false
        :param key: Key to search the table for
        :return: Either the node in the table with the given key or False if key is not found.
        """

        # for i in range(len(self.table)):
        #     # Compute the bucket index
        #     bucket = (self.hash_function(key) + (i * i)) % self.capacity
        #
        #     # An empty-since-start bucket stops the search
        #     if self.table[bucket] is None:
        #         break
        #
        #     if self.table[bucket] is not None:
        #         temp_node = self.table[bucket]
        #         if temp_node.key == key:
        #             # Found item with matching key. Return item.
        #             return temp_node
        #
        # # An item with the specified key was not found
        # return False

        index = self.hash_function(key)
        temp_node = self.table[index]

        if temp_node is None:
            return False

        if temp_node.key == key:
            return temp_node
        else:
            counter = 1
            while counter < self.capacity:
                old_position = index
                index = (old_position + (counter * counter)) % self.capacity
                temp_node = self.table[index]
                if temp_node is not None and temp_node.key == key:
                    return temp_node
                else:
                    counter += 1
            return False

    def lookup(self, key):
        """
        Searches for a given key in the Hash Table. If found, return the value with the given key.
        Otherwise, return false
        :param key: Key to search the table for
        :return: Either the value of the node in the table with the given key or False if key
        is not found.
        """
        index = self.hash_function(key)
        temp_node = self.table[index]

        if temp_node is None:
            return False

        if temp_node.key == key:
            node = self.table[index]
            return node.value
        else:
            counter = 1
            while counter < self.capacity:
                old_position = index
                index = (old_position + (counter * counter)) % self.capacity
                temp_node = self.table[index]
                if temp_node is not None and temp_node.key == key:
                    node = self.table[index]
                    return node.value
                else:
                    counter += 1
            return False

    def delete(self, key):
        """
        Delete a node with the given key from the Hash Table by setting it to None.
        :param key: Key of node to delete
        :return: No return
        """
        index = self.hash_function(key)
        temp_node = self.table[index]

        if temp_node is None:
            return

        if temp_node.key == key:
            self.table[index] = None
            self.size -= 1
        else:
            counter = 1
            while counter < self.capacity:
                old_position = index
                index = (old_position + (counter * counter)) % self.capacity
                temp_node = self.table[index]
                if temp_node is not None and temp_node.key == key:
                    self.table[index] = None
                    self.size -= 1
                    break
                else:
                    counter += 1
            return

    def grow(self):
        """
        Doubles capacity and rehashes all items in table
        :return: No return
        """
        self.capacity = self.capacity * 2
        self.rehash()

    def rehash(self):
        """
        Rehashes all items inside of the table
        :return: No return
        """
        new_table = [None]*self.capacity  # "A list is allowed within rehash"

        for element in self.table:
            temp_node = element
            if temp_node is not None:
                index = self.hash_function(temp_node.key)
                if new_table[index] is not None:
                    index = self.quadratic_probe(temp_node.key)
                new_table[index] = temp_node
        self.table = new_table

# make a class
ht = HashTable()
