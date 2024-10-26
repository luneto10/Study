graph = [
        [1, 3],  # Neighbors of node 0
        [0, 2, 4],  # Neighbors of node 1
        [1, 5],  # Neighbors of node 2
        [0],  # Neighbors of node 3
        [1, 5],  # Neighbors of node 4
        [2, 4]   # Neighbors of node 5
    ]

def dfs(graph, start_node, visited = None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    print(str(start_node) + " -> ", end="")
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited


dfs(graph, 0)