from linked_list import LinkedList

class HashTable(object):

    def __init__(self, items = None):
        """Initialize this HashTable and set items if specified"""

        self.slots = [LinkedList() for i in range(8)] # start with 8 slots
        self.size = 0

    def _get_hash_index(self, key):
        """Return a hash index by hashing the key and finding the remainder of the hash
        divided by the number of slots in the HashTable"""

        # knowing that the number of buckets will always be a power of 2
        # we can use bitwise AND `hash & l-1` instead of modulo
        return self._hash_str(key) & (len(self.slots)-1)

    def _hash_str(self, string):
        """Return a hash of the given string. hash_str uses the djb2 algorithm to compute
        the hash value of a string http://www.cse.yorku.ca/~oz/hash.html"""
        hash = 5381
        for char in string[1:]:
            # (hash << 5) + hash is equivalent to hash * 33
            hash = (hash << 5) + hash + ord(char)
        return hash

    def get_items(self):
        """Return a list of tuples representing all the items in the HashTable"""
        return [items.extend(slot.items()) for slot in self.slots]

    def contains(self, key):
        """Return True if the key is found in the HashTable,
        otherwise return False"""

        # get the slot (linked_list) the key belongs to
        # using our _get_hash_index function
        slot = self.slots[self._get_hash_index(key)]

        # look for key in linked list
        # if found return True, otherwise return False
        if slot.find_by_key(key) is not None:
            return True
        else:
            return False

    def get(self, key):
        """Return data found by given key in the HashTable,
        return None if key is not found"""

        # get the slot (linked_list) the key belongs to
        # using our _get_hash_index function
        slot = self.slots[self._get_hash_index(key)]

        # find key in linked list and return
        return slot.find_by_key(key)

    def set(self, key, value):
        """Add an item to the HashTable by key and value"""

        # get the slot (linked_list) the key belongs to
        # using our _get_hash_index function
        slot = self.slots[self._get_hash_index(key)]

        # if the item isn't already in the hash table,
        # increment size (delete item if it is)
        if not slot.delete_by_key(key):
            self.size += 1

        # append item to end of slot (linked list)
        slot.append((key, value))

        # if load factor exceeds 0.66, resize
        if (self.size / len(self.slots)) > 0.66:
            self._resize()

    def delete(self, key):
        """Remove an item from the HashTable by key or raise KeyError if key
        is not found in the HashTable"""

        # get the slot (linked_list) the key belongs to
        # using our _get_hash_index function
        slot = self.slots[self._get_hash_index(key)]

        # delete item or throw key error if item was not found
        if slot.delete_by_key(key):
            self.size -= 1
        else:
            raise KeyError('Key {} not found in HashTable'.format(key))

    def _resize(self):
        """"Resize the HashTable by doubling the number of slots and rehashing all items"""

        # get a list of all items in the hash table
        items = self.get_items()

        # reset size for hash table
        self.size = 0

        # generate new slots of double current slots
        self.slots = [LinkedList() for i in range(len(self.slots) * 2)]

        # rehash each item
        for key, value in items:
            self.set(key, value)
