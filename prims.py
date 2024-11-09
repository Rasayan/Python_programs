import sys

def prims_algo(graph):

    num_vertices = len(graph)
    parent = [-1] * num_vertices            # Aray to store MST
    key = [sys.maxsize] * num_vertices      # Key value(s) for min weight
    mst_set = [False] * num_vertices        # Keep track of vertices

    key[0] = 0

    for _ in range(num_vertices):
        min_key = sys.maxsize
        u = -1

        for v in range(num_vertices):
            if key[v] < min_key and not mst_set[v]:
                min_key = key[v]
                u = v

        mst_set[u] = True

        for v in range(num_vertices):

            if graph[u][v] and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("Edge  \tWeight")
    for i in range(1, num_vertices):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prims_algo(graph)