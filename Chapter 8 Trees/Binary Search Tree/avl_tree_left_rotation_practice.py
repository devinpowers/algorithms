class Node(object):

    def __init__(self, data = None):

        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1



class BST:

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:

            self.root = Node(data)

        else:
            self._insert(data,self.root)

    def _insert(self, data, current_node):

        if data < current_node.data:

            if current_node.left is None:

                current_node.left = Node(data)

                current_node.left.parent=current_node

            else:
                self._insert(data, current_node.left)

        elif data > current_node.data:

            if current_node.right is None:

                current_node.right = Node(data)

                current_node.right.parent=current_node



            else:
                self._insert(data, current_node.right)

        else:
            print("Value is Already present in Tree.")

    def print_tree(self):
        
        if self.root != None:
            
            self._print_tree(self.root)
     
        
    def _print_tree(self, current_node):
        
        if current_node != None:
            
            self._print_tree(current_node.left)
            print(str(current_node.data))
            self._print_tree(current_node.right)

    

    def getHeight(self, root):
        if not root:
            return 0
        
        return root.height
    
    def getBalanced(self, root):
        
        if not root:
            return
        
        return self.getHeight(root.left) - self.getHeight(root.right)
    
  


  


bst = BST()

bst.insert(10)
bst.insert(3)
bst.insert(109)
bst.insert(2)
bst.insert(6)
bst.insert(9)
bst.insert(110)
bst.insert(1)

bst.insert(69)


print(bst.print_tree())

