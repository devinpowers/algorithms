

class TreeNode:
    
    def __init__(self, data):
        
        self.data = data
        
        self.childern = []
        
        self.parent = None
    
    def add_child(self,child):
        
        child.parent = self
        
        self.childern.append(child)
        
    def print_tree(self):
        print(self.data)
        if self.childern:
            for child in self.childern:
                child.print_tree()
            
def build_product_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    
    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode('iphone'))
    cellphone.add_child(TreeNode('Google Pixel'))
    cellphone.add_child(TreeNode('Vivo'))
    
    
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    
        
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root
    

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass
