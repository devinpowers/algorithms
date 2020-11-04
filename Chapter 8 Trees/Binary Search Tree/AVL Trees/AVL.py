import math

class Node(object):
    
   def __init__(self, value = None):
        
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
        


class AVL_Tree():
    
    def __init__(self):
        
        self.root = None
    
        
    def insert(self,value):
        
        if self.root == None:
            
            self.root = Node(value)
        
        else:
            self._insert(value, self.root)
        
    def insert(self, value, current_node):
        
        if value < current_node.value:
            
            if current_node.left == None:
                
                current_node.left = Node(value)
                
                
                current_node.left.parent = current_node # Set the Parent
                self._inspect_insertion(current_node.left) # Added Feature to check balance
            
            else:
                self._insert(value, current_node.left)
        
        elif value > current_node.value:
            
            if current_node.right == None:
                current_node.right = Node(value)
                
                
                current_node.right.parent = current_node # Set Parent
            
                self._inspect_insertion(current_node.right) # added feature to check balance of insertion
            
            else:
                self._inser(value, current_node.right)
        
        else:
            print("The Value is already in the AVL Tree")
     
    def print_tree(self):
        
        if self.root != None:
            self._print_tree(self.root)
            
    def _print_tree(self,current_node):
        
        '''Print out Height of the tree and its Value'''
        
        if current_node != None:
            
            self._print_tree(current_node.left)
            print("Current Node Value:", current_node.value)
            print("Current Node Height:", current_node.height)
            self._print_tree(current_node.right)

            
    def delete_value(self,value):
        
        return self.delete_node(self.find(value))
        
        
    def delete_node(self, node):
        
        # IN case Node doesnt exisit in the tree or no elemnts in the tree
        if node == None or self.find(node.data) == None:
            
            print("Node to be deleted doesnt exist and isnt in the tree")
            return None
        
        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            
            current = n
            
            while current.left != None:
                
                current = current.left
            return current
        
        # returns the number of children for the specified node
        def number_childern(n):
            
            number_childern = 0
            
            if n.left != None:
                
                number_childern += 1
                
            if n.right != None:
                
                number_childern += 1
            
            return number_childern
    
        
    	# get the parent of the node to be deleted
        
        node_parent = node.parent
        
		# get the number of children of the node to be deleted
        
        node_childern = number_childern(node)
        # break operation into different cases based on the
		# structure of the tree & node to be delete
		# CASE 1 (node has no children)
        
        if node_childern == 0:
            
            # Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
            
            if node_parent != None:
                # remove reference to the node from the parent
                
                if node_parent.left == node:
                    node_parent.left = None
                
                else:
                    node_parent.right = None
            
            else:
                self.root = None
                
            
        # CASE 2 (node has a single child)
        
        if node_childern == 1:
            
            # get the single child node
            
            if node.left != None:
                
                child = node.left
                
            else:
                child = node.right
                
            # deleted the root node it would delete entire tree.
            
            if node_parent != None:
                # replce the node to be deleted with its child
                
                if node_parent.left_child == node:
                    
                    node_parent.left = child
                    
                else:
                    node_parent.right = child
            
            else:
                self.root = child
                
            
            #correct the parent parent in node
            child.parent = node_parent
        
        # CASE 3 (node has two children)
        if node_childern == 2:
            
            # get inorder sucessof of the deleted node
            
            sucessor = min_value_node(node.right)
            
            #copy the inorder successor's value to the node
            #formerly holding the value we wished to delete
            
            node.data = sucessor.data
            
            #delete the inorder sucessor now that it's value
            #was copied into th other node
            
            self.delete_node(sucessor)
            
        if node_parent != None:



        
     def height(self):
        
        
         if self.root != None:
            
             return self._height(self.root, 0)
        
         else:
            
             return 0
        
            
    def height(self):
    
        if self.root != None:
            
            return self._height(self.root, 0)
        
        else:
            
            return 0
        
    def _height(self, current_node, current_height):
        
        if current_node == None:
            return current_height
        
        left_height = self._height(current_node.left, current_height)
        
        right_height = self._height(current_node.right, current_height)
        
        return max(left_height, right_height)

    # Functions added for AVL...
    
    def _inspect_insertion(self, current_node, path = [] ):
        
        if current_node.parent == None:
            return
        
        path = [current_node] + path
        
        left_height = self.get_height(current_node.parent.left)
        
        right_height = self.get_height(current_node.parent.right)
        
        if abs(left_height - right_height) > 1:
            
            path = [current_node.parent] + path
            
            self._rebalance_node(path[0], path[1], path[2])
            
            return
        
        new_height = 1 + current_node.height
        
        if new_height > current_node.parent.height:
            
            current_node.parent.height = new_height
        
        self._inspect_insertion(current_node.parent, path)

    
    def _rebalance_node(self, z, y, x):
        
        if y == z.left and x == y.left:
            
            self._right_rotate(z)
        
        elif y == z.left and x == y.right:
            
            self._left_rotate(y)
            self._right_rotate(z)
            
        elif y == z.
        
        
        
        
        
        
            

    
    
    
    