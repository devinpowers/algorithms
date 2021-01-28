
## Seperate Chaining!!!
'''Seperate Chaining (Using Linked Lists!) to handle Collisions'''


class Node:
    '''Hash Table node, part of Linked List'''
    '''each Bucket will contain a linked list of nodes containing
    the objects stored at that index'''
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
    def __str__(self):
        """Retun a string representation of the Object"""
        return "<Node: (%s, %s), next: %s> \t" % (self.key, self.value, self.next != None)
    
    def __repr__(self):
        return str(self)
        

class HashTable:
    """ Initialize our Hash Table"""
    def __init__(self):
       
        self.capacity = 5   
        self.size = 0       # Number of nodes
        self.buckets = [None]*self.capacity      # Number of Buckets in HashTable
        
    
    def hash(self, key):
        
        '''Hash Function will take our Keys and give a index for our Buckets Array! '''
        '''We want our hash values to be evenly distributed among our Buckets '''
        '''Paramater is the Key, will return a hash_sum which will be used to index  '''
        
        hash_sum = 0
        
        for index, c in enumerate(key):
            
            hash_sum += (index + len(key)) ** ord(c)
            
            hash_sum = hash_sum % self.capacity
    
            
        return hash_sum
        
    def length(self):
        '''Returns the Size, which is the of Node in HashTable'''
        return self.size
    
    def insert(self, key, value ):
        
        ''' Parameters: Key and Value, a key for the new item and Value for new item'''
        
        self.size += 1
        
        index = self.hash(key)
                
        node = self.buckets[index]
        
        if node is None:
            
            self.buckets[index] = Node(key, value)   
            
            return
        
        prev = node
        while node is not None: #loop through linked list
            
            prev = node
            node = node.next
        
        prev.next = Node(key,value)
        
    
    def find(self, key):
        
        '''Returns Value of our Key we pass in to find, Returns False if the Key doesnt exist'''
        
        index = self.hash(key)
        
        node = self.buckets[index]
        
        while node is not None and node.key != key:
            node = node.next
        
        if node is None:
            
            return False 
        else:
            # Found and return the data value
            
            return node.value
        
    
    def delete(self, key):
        
        '''Remove association from Our map'''
        '''Parameter is the Key of the pair we want to Delete'''
        
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        
        while node is not None and node.key != key:
            prev = node
            node = node.next
            
        
        if node is None:
            return None
        
        else:
            
            self.size -= 1
            result = node.value
            
            if prev is None:
                self.buckets[index] = node.next
            
            else:
                prev.next = prev.next.next 
                
            return result


ht = HashTable()


## lets inserted values into our hash Table
        
                                    
heat = ["Lebron", "Wade", "Bosh"]

pistons = ["Wallace", "Billups", "Hamilton", "Prince"]

bulls =["Jordan", "Pippin", "Rose"]

bucks = ["Giannas", "Redd", "Allen"]

clippers = ["Griffin", "Paul"]

hawks = ["Trae", "Horford"]

lakers = ["Kobe", "Shaq", "Gasol"]

warriors = ["Curry", "Klay", "Green"]

jazz = ["Mitchell", "Gobert"]

suns = [ "Booker", "Paul", "Ayton"]

ht.insert("Pistons", pistons)
ht.insert("Bulls", bulls)
ht.insert("Bucks", bucks)
ht.insert("Clippers", clippers)
ht.insert("Hawks", hawks)
ht.insert("Lakers", lakers)
ht.insert("Warriors", warriors)
ht.insert("Jazz", jazz)
ht.insert("Suns", suns)




## Lets see if we can find Bucks?

print(ht.find("Bucks"))
print(ht.find("Lakers"))
print(ht.find("Bucks"))
print(ht.find("Hawks"))
print(ht.find("Suns"))




print("\n")
print("Size of our Hash Table is:", ht.size)









































