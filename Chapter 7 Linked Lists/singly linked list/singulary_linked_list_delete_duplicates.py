# YouTube Link: https://www.youtube.com/watch?v=s9NEaxVvQnQ
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node 
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    '''swap by changing the next attribute of node'''
    
    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return 

        previous_1 = None 
        current_1 = self.head 
        
        while current_1  and current_1 .data != key_1:
            previous_1 = current_1  
            current_1  = current_1.next

        previous_2 = None 
        current_2 = self.head 
        
        while current_2 and current_2.data != key_2:
            previous_2 = current_2 
            current_2 = current_2.next

        if not current_1 or not current_2:
            return 

        if  previous_1:
             previous_1.next = current_2
        else:
            self.head = current_2

        if previous_2:      
           previous_2.next = current_1       
        else:
            self.head = current_1
      
        # swap Node.Next of Node 1 and Node 2 (current_1 and current_2 )
        current_1.next,current_2.next = current_2.next,  current_1.next
        

    ''' Alternate swap node function , swap by changing the data attribute of node '''
    def swap_nodes_alt(self, key_1, key_2):
        if key_1 == key_2:
            return
        curr  = self.head
        x , y = None , None # Assign None to avoid reference error
        while curr :
            if curr.data == key_1:
                x = curr # key_1 found
            if curr.data == key_2:
                y =curr # key_2 found
            curr = curr.next
        
        if x and y: # Check if both key's exist
            x.data , y.data = y.data , x.data
        else : 
            return
    
    
    def remove_duplicates(self):
        
        current = self.head
        previous = None
        
        duplicate_values = dict()
        
        while current:
            
            if current.data in duplicate_values:
                
                # Remove node:
                previous.next = current.next
                current = None
            
            else:
                # have note encountered element before
                duplicate_values[current.data] = 1
                previous = current
            
            current = previous.next
            
            
        

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("D")
llist.append("F")
llist.append("G")

print("Initial list")
llist.print_list()

llist.remove_duplicates()

print('List after duplicate deletion')
llist.print_list()





