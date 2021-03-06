


class Queue:

    def __init__(self):
        self.queue = []
        self.size = 0;

    def enqueue(self, item):
        """Add to Queue"""
        self.queue.append(item)
        self.size += 1

    def dequeue(self):
        """pop/remove from Queue"""
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
        self.size -= 1
    
        
    def is_empty(self):
        "Return True if the queue is empty"
        return self.size == 0
    


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
        
    
    def degree(self,node):
        '''Total number of edges coming out a given node'''
        deg = len(self.adj_list[node])
        return deg
    
    def print_adj_list(self):
        
        for node in self.nodes:
            print(node, "->", self.adj_list[node])
    
    def __getitem__(self, node):
        
        """retrives items from out Node/vertex"""
        
        return  self.adj_list[node]
    
            
all_edges = [ 
    
    ("A","B"), ("A","E"), ("B","E"), ("E","D"), ("B","D"), ("A","C"), ("C","F"), ("C","G")
]
nodes = ["A","B","C","D","E", "F", "G"]


graph1 = Graph(nodes)

for u,v in all_edges:
    graph1.add_edge(u,v)

graph1.print_adj_list()



def bfs(graph, start):
    # keep track of all visited nodes
    visited = []
    queue = Queue()
    queue.enqueue(start)
 
    # keep looping until there are nodes still to be checked
    
    while not queue.is_empty():
    
        node = queue.dequeue()
        
        if node is None:
            break
        
        if node not in visited:
            
            visited.append(node)
            
            neighbours = graph[node]
 
            for neighbour in neighbours:
                
                queue.enqueue(neighbour)
                
    return visited





print("Breadth First Search, Nodes visited: ")
print(bfs(graph1,"A") )


