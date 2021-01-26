

## Hash

# create a new HashTable

INITIAL_CAPACITY = 5
# Node data structure - essentially a LinkedList node

long num = 9;


class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
	def __str__(self):
		" Return a string representation of the Object "
		return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
	def __repr__(self):
		return str(self)

# Hash Table with seperate chaining


class HashTable:
	# Initialize hash table
	def __init__(self):
		self.capacity = INITIAL_CAPACITY
		self.size = 0
		self.buckets = [None]*self.capacity
	# Generate a hash for a given key
	# Input:  key - string
	# Output: Index from 0 to self.capacity
	def hash(self, key):
		hashsum = 0
		# For each character in the key
		for idx, c in enumerate(key):
			# Add (index + length of key) ^ (current char code)
			hashsum += (idx + len(key)) ** ord(c)
			# Perform modulus to keep hashsum in range [0, self.capacity - 1]
			hashsum = hashsum % self.capacity
		return hashsum

	# Insert a key,value pair to the hashtable
	# Input:  key - string
	# 		  value - anything
	# Output: void
	def insert(self, key, value):
		# 1. Increment size
		self.size += 1
		# 2. Compute index of key
		index = self.hash(key)
		# Go to the node corresponding to the hash
		node = self.buckets[index]
		# 3. If bucket is empty:
		if node is None:
			# Create node, add it, return
			self.buckets[index] = Node(key, value)
			return
		# 4. Iterate to the end of the linked list at provided index
		prev = node
		while node is not None:
			prev = node
			node = node.next
		# Add a new node at the end of the list with provided key/value
		prev.next = Node(key, value)

	# Find a data value based on key
	# Input:  key - string
	# Output: value stored under "key" or None if not found
	def find(self, key):
		# 1. Compute hash
		index = self.hash(key)
		# 2. Go to first node in list at bucket
		node = self.buckets[index]
		# 3. Traverse the linked list at this node
		while node is not None and node.key != key:
			node = node.next
		# 4. Now, node is the requested key/value pair or None
		if node is None:
			# Not found
			return None
		else:
			# Found - return the data value
			return node.value

	# Remove node stored at key
	# Input:  key - string
	# Output: removed data value or None if not found
	def remove(self, key):
		# 1. Compute hash
		index = self.hash(key)
		node = self.buckets[index]
		prev = None
		# 2. Iterate to the requested node
		while node is not None and node.key != key:
			prev = node
			node = node.next
		# Now, node is either the requested node or none
		if node is None:
			# 3. Key not found
			return None
		else:
			# 4. The key was found.
			self.size -= 1
			result = node.value
			# Delete this element in linked list
			if prev is None:
				self.buckets[index] = node.next # May be None, or the next match
			else:
				prev.next = prev.next.next # LinkedList delete by skipping over
			# Return the deleted result 
			return result
	

ht = HashTable()



# create some data to be stored

#phone_numbers = ["616-914-8235", "616-364-1338"]

names = ["Devin", "Austin", "Abe", "Lebron", "Chris"]

heat = ["Lebron", "Wade", "Bosh"]

pistons = ["Wallace", "Billups", "Hamilton", "Prince"]

bulls =["Jordan", "Pippin", "Rose"]

bucks = ["Giannas", "Redd", "Allen"]

clippers = ["Griffin", "Paul"]

knicks = ["Melo", "noah", "Fisher", "Tommy", "SIDS"]

#ht.insert("PhoneDirectory", phone_numbers)

ht.insert("Names", names)
ht.insert("Pistons", pistons)
ht.insert("Bulls", bulls)
ht.insert("Bucks", bucks)
ht.insert("Clippers", clippers)
ht.insert("Knicks", knicks)



value = ht.find("Clippers")

print(value)



##numbers = ht.find("PhoneDirectory")

##rint(numbers)






























