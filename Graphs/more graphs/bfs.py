# Breadth First Search (BFS) Algorithm

from queue import Queue

def bfs(graph, start):
    visited = []
    queue = Queue()
    queue.put(start)
    
    while not queue.empty():
        vertex = queue.get()
        if vertex not in visited:
            visited.append(vertex)
            for vert in graph[vertex]:
                if vert not in visited:
                    queue.put(vert)
            
    return visited


if __name__ == '__main__':
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
    
    visited = bfs(graph,'A')
    print(visited)