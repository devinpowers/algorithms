class Node:
    
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node 

        else:
            new_node = Node(data)
            cur = self.head 
            while cur.next:
                cur = cur.next 
            cur.next = new_node 
            new_node.prev = cur 
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def add_after_node(self, key, data):
        
        current = self.head
        
        while current:
            
            if current.next is None and current.data == key:  # Case One
                
                self.append(data)
                return
                
            elif current.data == key:
                
                new_node = Node(data)
                
                nxt = current.next 
                
                current.next = new_node
                
                new_node.next = nxt
                
                nxt.previous = new_node
                
                new_node.prev = current
                
            current = current.next
            
            

    def add_before_node(self, key, data):
        
        current = self.head 
        
        while current:
            if current.prev is None and current.data == key:
                
                self.prepend(data)
                
            elif current.data == key:
                
                new_node = Node(data)
                
                prev = current.prev
                
                prev.next = new_node
                
                current.prev = new_node
                
                new_node.next = current
                
                new_node.prev = prev
                
            current = current.next


    def print_list(self):
        cur = self.head 
        while cur:
            print(cur.data)
            cur = cur.next
    
    def delete(self, key):
        
        current = self.head
        
        while current:
            if current.data == key and current == self.head:
                # Case 1:
                if not current.next:
                    current = None 
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = current.next
                    current.next = None 
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return 

            elif current.data == key:
                # Case 3:
                if current.next:
                    nxt = current.next 
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None 
                    current.prev = None
                    current = None
                    return

                # Case 4:
                else:
                    prev = current.prev 
                    prev.next = None 
                    current.prev = None 
                    current = None 
                    return 
             current = current.next


dllist = DoublyLinkedList()

dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)





#dllist.add_after_node(1,11)
#dllist.add_after_node(3,14)
#dllist.add_after_node(4,69)

dllist.add_before_node(4,69)
dllist.add_before_node(3,23)
dllist.add_before_node(2,59)




dllist.print_list()