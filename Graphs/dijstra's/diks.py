

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

    def __len__(self):

        return len(nodes)


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

    (1,2),(1,3),(2,4),(3,4),(3,5),(4,5)
]
nodes = [1,2,3,4,5]

graph1 = Graph(nodes)
#graph1.print_adj_list()

for u,v in all_edges:
    graph1.add_edge(u,v)

##graph.add_edge("A","B")
graph1.print_adj_list()







def dijkstra(graph, start):
    """
    Implementation of dijkstra using adjacency matrix.
    This returns an array containing the length of the shortest path from the start node to each other node.
    It is only guaranteed to return correct results if there are no negative edges in the graph. Positive cycles are fine.
    This has a runtime of O(|V|^2) (|V| = number of Nodes), for a faster implementation see @see ../fast/Dijkstra.java (using adjacency lists)

    :param graph: an adjacency-matrix-representation of the graph where (x,y) is the weight of the edge or 0 if there is no edge.
    :param start: the node to start from.
    :return: an array containing the shortest distances from the given start node to each other node
    """
    # This contains the distances from the start node to all other nodes
    distances = [float("inf") for _ in range(len(graph))]

    # This contains whether a node was already visited
    visited = [False for _ in range(len(graph))]

    # The distance from the start node to itself is of course 0
    distances[start] = 0

    # While there are nodes left to visit...
    while True:

        # ... find the node with the currently shortest distance from the start node...
        shortest_distance = float("inf")
        shortest_index = -1
        for i in range(len(graph)):
            # ... by going through all nodes that haven't been visited yet
            if distances[i] < shortest_distance and not visited[i]:
                shortest_distance = distances[i]
                shortest_index = i

        # print("Visiting node " + str(shortest_index) + " with current distance " + str(shortest_distance))

        if shortest_index == -1:
            # There was no node not yet visited --> We are done
            return distances

        # ...then, for all neighboring nodes that haven't been visited yet....
        for i in range(len(graph[shortest_index])):
            # ...if the path over this edge is shorter...
            if graph[shortest_index][i] != 0 and distances[i] > distances[shortest_index] + graph[shortest_index][i]:
                # ...Save this path as new shortest path.
                distances[i] = distances[shortest_index] + graph[shortest_index][i]
                # print("Updating distance of node " + str(i) + " to " + str(distances[i]))

        # Lastly, note that we are finished with this node.
        visited[shortest_index] = True
        # print("Visited nodes: " + str(visited))
        # print("Currently lowest distances: " + str(distances))


dijkstra(graph1, 1)
