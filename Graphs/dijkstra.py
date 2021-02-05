# Finding the shortest path using Dijkstra algorithm
# Weighted Undirected Graph

import sys

class Vertex:
    
    ''' For each vertex five attributes are defined: id, dictionary of ajacent
    vertices, distance (initiated with infinity), visited (initiated with False
    ), and predecessor (initiated with None). The last three attributes are
    reserved for BFS/DFS purposes'''
    
    def __init__(self, vertex):
        self.id = vertex
        self.adjacent = dict()
        self.distance = sys.maxsize        
        self.visited = False  
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    
    ''' Adjacency List representation. We keep a master list of vertex objects'''
    
    def __init__(self):
        self.master_list = dict()
        self.num_vertices = 0

    def add_vertex(self, vert):
        self.num_vertices += 1
        self.master_list[vert] = Vertex(vert)
        return Vertex(vert)

    def get_vertex(self, v):
        if v in self.master_list:
            return self.master_list[v]
        else:
            return None

    def add_edge(self, fromV, toV, cost = 0):
        if fromV not in self.master_list:
            self.add_vertex(fromV)
        if toV not in self.master_list:
            self.add_vertex(toV)
        
        # undirected graph
        self.master_list[fromV].add_neighbor(self.master_list[toV], cost)
        self.master_list[toV].add_neighbor(self.master_list[fromV], cost)

    def get_vertices(self):
        return self.master_list.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous
    
    def __iter__(self):
        return iter(self.master_list.values())


def shortest(target, path = None):
    ''' make shortest path from v.previous'''
    if path == None:
        path = [target]
        target = g.get_vertex(target)
        
    if target.previous:
        path.append(target.previous.get_id())
        shortest(target.previous, path)
    
    return path[::-1]


def dijkstra(graph, source):
    '''Dijkstra's shortest path'''
    
    start = graph.get_vertex(source)
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in graph]
    unvisited_queue = sorted(unvisited_queue, key = lambda x: x[0])
    

    while len(unvisited_queue):
        # Pop a vertex with the smallest distance from the queue
        exploring_vertex = unvisited_queue.pop(0)
        current = exploring_vertex[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue  # returns the control to  beginning of the WHILE loop
            
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
            else:
                pass

        # Rebuild the unvisited list
        unvisited_queue = [(v.get_distance(),v) for v in graph if not v.visited]
        unvisited_queue = sorted(unvisited_queue, key = lambda x: x[0])
    


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('V0')
    g.add_vertex('V1')
    g.add_vertex('V2')
    g.add_vertex('V3')
    g.add_vertex('V4')
    g.add_vertex('V5')

    g.add_edge('V0', 'V1', 5)  
    g.add_edge('V0', 'V5', 2)
    g.add_edge('V1', 'V2', 4)
    g.add_edge('V2', 'V3', 9)
    g.add_edge('V3', 'V4', 7)
    g.add_edge('V3', 'V5', 3)
    g.add_edge('V4', 'V0', 1)
    g.add_edge('V5', 'V4', 8)
    g.add_edge('V5', 'V2', 1)


    dijkstra(g, source = 'V1')
    sp = shortest(target = 'V3')
    print( 'The shortest path : %s' %(sp))
    print( 'The shortest distance : %s' %(g.get_vertex(sp[-1]).distance))