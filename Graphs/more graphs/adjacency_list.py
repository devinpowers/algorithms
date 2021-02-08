




class Graph:
    
    def __init__(self, Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        
        self.is_directed = is_directed
        
        for node in self.nodes:
            self.adj_list[node] = []
    
    def print_adj_list(self):
        
      for node in self.nodes:
          print(node, "->", self.adj_list[node])
            
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
      
      
        if not self.is_directed:
            
            self.adj_list[v].append(u)
        
        
    
    def degree(self,node):
        '''Total number of edges coming out a given node'''
        deg = len(self.adj_list[node])
        return deg
    
  
    

all_edges = [
    
    ("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")
]



nodes = ["A","B","C","D","E"]

graph = Graph(nodes)

print("\nGraph before we add the edges: ")
graph.print_adj_list()


for u,v in all_edges:
    graph.add_edge(u,v)

print("\nGraph after adding edges: " )
graph.print_adj_list()


print("\nDegree of C: ", graph.degree("C"))

print("Degree of B: ", graph.degree("B"))


graph2 = Graph(nodes, is_directed = True)

for u,v in all_edges:
    graph2.add_edge(u,v)

print("\nGraph 2 with Directed")
graph2.print_adj_list()

