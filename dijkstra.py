import sys

def dijkstra(graph, src):
    num_vertices = len(graph)
    
    dist = [sys.maxsize] * num_vertices 
    
    dist[src] = 0
    
    spt_set = [False] * num_vertices
    
    for _ in range(num_vertices):
        min_dist = sys.maxsize
        u = -1
        
        for v in range(num_vertices):
            if not spt_set[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v

        spt_set[u] = True

        for v in range(num_vertices):
            if graph[u][v] > 0 and not spt_set[v] and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print("Vertex \tDistance from Source")
    for i in range(num_vertices):
        print(f"{i} \t{dist[i]}")

graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

dijkstra(graph, 0)
