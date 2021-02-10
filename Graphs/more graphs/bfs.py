
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B',"E"],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    print("explored", explored)
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        
        print("Node:", node)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                print("Neighbour added: ", neighbour)
                queue.append(neighbour)
    return explored

answer = bfs_connected_component(graph,'A')
print(answer)


