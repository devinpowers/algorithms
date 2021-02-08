# Depth First Search (DFS) Algorithm



graph = {'A': set(['B', 'C']),
     'B': set(['A', 'D', 'E']),
     'C': set(['A', 'F']),
     'D': set(['B']),
     'E': set(['B', 'F']),
     'F': set(['C', 'E'])}



def dfs(graph,start):
    visited = set()
    stack = [start]
    
    while stack: ## isnt empty
        
        vertex = stack.pop() ## pop vertex/node from stack
        
        print("Vertex:", vertex)
        if vertex not in visited: ## 
            
            visited.add(vertex) 
            
            
            stack.extend(graph[vertex]-visited)
            
            #print(stack)
            
    return visited


# dfs with graph and D which is the starting point

vis = dfs(graph,'C')
print(vis)


