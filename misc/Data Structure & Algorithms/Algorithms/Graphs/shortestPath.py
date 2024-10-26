from collections import deque

def shortest_path(graph, start_node, end_node):
    visited = set({start_node})
    queue = deque([start_node])
    parents = {start_node : None}
    
    while queue:
        current_node = queue.popleft()
        for neighboor in graph[current_node]:
            if neighboor not in visited:
                visited.add(neighboor)
                queue.append(neighboor)
                parents[neighboor] = current_node

    current_node = end_node
    path = []
    while current_node is not None:
        path.append(current_node)
        current_node = parents[current_node]
    path.reverse()
    return path

graph = [
        [1, 3],  # Neighbors of node 0
        [0, 2, 4],  # Neighbors of node 1
        [1, 5],  # Neighbors of node 2
        [0],  # Neighbors of node 3
        [1, 5],  # Neighbors of node 4
        [2, 4]   # Neighbors of node 5
    ]
print(shortest_path(graph, 0, 5))

graph_letters = {
    "A": ["B", "C", "D"],  # Neighbors of node A
    "B": ["A", "E"],  # Neighbors of node B
    "C": ["B", "F"],  # Neighbors of node C
    "D": ["A"],       # Neighbors of node D
    "E": ["B", "F"],  # Neighbors of node E
    "F": ["C", "E"]   # Neighbors of node F
}

def shortest_path(graph, start_node, end_node):
    visited = set({start_node})
    queue = deque([start_node])
    parents = {start_node : None}
    
    while queue:
        current_node = queue.popleft()
        for neighboor in graph[current_node]:
            if neighboor not in visited:
                visited.add(neighboor)
                queue.append(neighboor)
                parents[neighboor] = current_node

    current_node = end_node
    path = []
    while current_node is not None:
        path.append(current_node)
        current_node = parents[current_node]
    path.reverse()
    return path

print(shortest_path(graph_letters, "A", "D"))

