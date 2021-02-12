# Finding the shortest path using Bellman-Ford algorithm
# Weighted Undirected Graph
import sys

def bellman_ford(graph, source):
    # Define an empty dictionary to store the distance and predecessor
    distance    = {}
    predecessor = {}
    
    for node in graph:
        distance[node]    = sys.maxsize
        predecessor[node] = None
    
    distance[source] = 0

    # Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                # Check the relation condition and update the distance and
                # predecessor dictionary
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour] = distance[node] + graph[node][neighbour]
                    predecessor[neighbour] = node
    
    # Negative weight cycle check
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle."
 
    return distance, predecessor
    
if __name__ == '__main__':
    
    # directed graph
    graph = {
        'V0': {'V1': 5, 'V5': 2},
        'V1': {'V2': 4},
        'V2': {'V3': 9},
        'V3': {'V4': 7, 'V5': 3},
        'V4': {'V0': 1},
        'V5': {'V2': 1, 'V4': 8}
    }

    distance, predecessor = bellman_ford(graph, source='V0')

    print(distance)
    
    # undirected graph
    graph = {
        'V0': {'V1': 5, 'V4': 1, 'V5': 2},
        'V1': {'V0': 5, 'V2': 4},
        'V2': {'V1': 4, 'V3': 9, 'V5': 1},
        'V3': {'V2': 9, 'V4': 7, 'V5': 3},
        'V4': {'V0': 1, 'V3': 7, 'V5': 8},
        'V5': {'V0': 2, 'V2': 1, 'V3':3, 'V4': 8}
    }
 
    distance, predecessor = bellman_ford(graph, source='V0')
    

    print(distance)