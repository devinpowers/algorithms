# Detect a cycle in a graph

def cycle_check(graph):
    status = {u : "unvisited" for u in graph}
    found_cycle = [False]


    for vert in graph:                         
        if status[vert] == "unvisited":
            dfs(graph, vert, status, found_cycle)
        if found_cycle[0]:
            break
    
    return found_cycle[0]

def dfs(graph, current_vertex, status, found_cycle):
    
    if found_cycle[0]:
        return
    
    status[current_vertex] = "visiting"
    
    for neighbor in graph[current_vertex]:
        if status[neighbor] == "visiting":
            found_cycle[0] = True       
            return
        
        if status[neighbor] == "unvisited":
            dfs(graph, neighbor, status, found_cycle)
    
    status[current_vertex] = "visited"     


if __name__ == '__main__':
    
    # undirected graph
    graph = {
        'V0': {'V1': 5, 'V4': 1, 'V5': 2},
        'V1': {'V0': 5, 'V2': 4},
        'V2': {'V1': 4, 'V3': 9, 'V5': 1},
        'V3': {'V2': 9, 'V4': 7, 'V5': 3},
        'V4': {'V0': 1, 'V3': 7, 'V5': 8},
        'V5': {'V0': 2, 'V2': 1, 'V3':3, 'V4': 8}
    }
    
    print('Is there a cycle in the graph? ', cycle_check(graph))
    
    # directed graph
    graph = {
        'V0': {'V1': 5, 'V5': 2},
        'V1': {'V2': 4},
        'V2': {'V3': 9},
        'V3': {'V4': 7, 'V5': 3},
        'V4': {'V0': 1},
        'V5': {'V2': 1, 'V4': 8}
    }
    print('Is there a cycle in the graph? ', cycle_check(graph))