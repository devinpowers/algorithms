# Finding the shortest path using Floyd-Warshall algorithm
# Weighted Undirected Graph

import sys 
inf = sys.maxsize

def floyd_warshall(distance_matrix):
    V = len(distance_matrix)
    distance_matrix = distance_matrix
    for k in range(V):
        next_distance_matrix = distance_matrix # create a copy for modification
        for i in range(V):
            for j in range(V):
                # examine if the kth vertex can create a shorter path between two vertices
                next_distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
        
        distance_matrix = next_distance_matrix # update the main copy
    return distance_matrix


    
if __name__ == '__main__':
    
    # A graph represented as Adjacency matrix
    distmat = [
    [0,     5,   inf,   inf,    inf,     2],
    [inf,   0,   4,     inf,    inf,     inf],
    [inf,   inf, 0,     9,      inf,     inf],
    [inf,   inf, inf,   0,      7,      3],
    [1,     inf, inf,   inf,    0,      inf],
    [inf,   inf, 1,     inf,    8,      0],
    ]

    print(floyd_warshall(distmat))