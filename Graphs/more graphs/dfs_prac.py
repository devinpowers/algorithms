"""Depth First Search"""


class Stack():

    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)				
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items
    
    def print_stack(self):
        
        for element in self.items:
            print(element)
    


class Graph:
    
    def __init__(self, Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        
        self.is_directed = is_directed
        
        for node in self.nodes:
            self.adj_list[node] = []
            
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        
        if not self.is_directed:
            
            self.adj_list[v].append(u)
            
    def size(self):
        return len(self.nodes)
        
    
    def degree(self,node):
        '''Total number of edges coming out a given node'''
        deg = len(self.adj_list[node])
        return deg
    
    def print_adj_list(self):
        
        for node in self.nodes:
            print(node, "->", self.adj_list[node])




def depth_first_search(graph, starting_node):
    
    
    # have to find size of the graph, number of nodes
    
    visted = set()
    print(visted)
    
    stack = Stack()  # creating a stack object
    
    stack.push(starting_node)
    
    while stack:
        
        vertex = stack.pop()
        
        if vertex not in visted:
            
            visted.add(vertex)
            #stack.push(graph[vertex]- visted)
        
    return visted


    


# need to populate our Graph:

nodes = ["A","B","C","D","E"]

g = Graph(nodes)

all_edges = [
    
    ("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")
]

for u,v in all_edges:
    g.add_edge(u,v)

print("\nGraph after adding edges: " )
g.print_adj_list()

### Now lets use the Depth First Search using our Graph g:
    
visted = depth_first_search(g, "A")













