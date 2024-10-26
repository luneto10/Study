from collections import deque
graph = [
        [1, 3],  # Neighbors of node 0
        [0, 2, 4],  # Neighbors of node 1
        [1, 5],  # Neighbors of node 2
        [0],  # Neighbors of node 3
        [1, 5],  # Neighbors of node 4
        [2, 4]   # Neighbors of node 5
    ]

def bfs_non_recursive(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    predecessor = {start_node: None}
    
    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                predecessor[neighbor] = current_node
                
    return predecessor

def shortest_path(graph, start_node, end_node):
    predecessor = bfs_non_recursive(graph, start_node)
    
    if end_node not in predecessor:
        return None
    
    path = []
    current_node = end_node
    while current_node is not None:
        path.append(current_node)
        current_node = predecessor[current_node]

    path.reverse()
    
    return path

print(shortest_path(graph, 0, 5))
    