
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

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, node):

        """retrives items from out Node/vertex"""

        return  self.adj_list[node]

    def __iter__(self):
        return iter(self.adj_list)


all_edges = [

    ("A","D"),("B","D"),("C","B"),("C","A"),("E","A"),("E","D"),
    ("E","F"),("D","H"),("D","G"),("F","K"),("F","J"),("H","J"),
    ("H","I"),("G","I"),("K","J"),("J","M"),("J","L"),("I","L")

]
nodes = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]

graph1 = Graph(nodes, is_directed = True)

for u,v in all_edges:
    graph1.add_edge(u,v)

graph1.print_adj_list()







D.addRear("A")
D.addRear("D")
D.addRear("C")
D.size()
