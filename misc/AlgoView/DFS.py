import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button

# Create a new graph
G = nx.Graph()

# Add edges to form a different graph structure
new_edges = [(0, 1), (0, 3), (1, 2), (1, 4), (2, 5), (3, 4), (4, 5), (5, 6), (6, 7), (6, 8)]
G.add_edges_from(new_edges)

# DFS Algorithm with preorder and postorder lists
def dfs(graph, start_node):
    visited = {node: False for node in graph.nodes()}
    traversal_order = []
    preorder = []  # List to store preorder traversal
    postorder = []  # List to store postorder traversal
    parent = {start_node: None}

    def dfs_visit(node):
        visited[node] = True
        traversal_order.append((node, 'visit'))  # Node visit
        preorder.append(node)  # Add to preorder list

        for neighbor in graph.neighbors(node):
            if not visited[neighbor]:
                parent[neighbor] = node
                dfs_visit(neighbor)

        # Backtrack step - after visiting all neighbors
        traversal_order.append((node, 'backtrack'))  # Node backtracking
        postorder.append(node)  # Add to postorder list

    dfs_visit(start_node)
    return traversal_order, preorder, postorder, parent

# Generate DFS traversal order with backtracking steps, preorder, and postorder
traversal_order, preorder, postorder, parent = dfs(G, 0)

# Initialize plot
fig, ax = plt.subplots(figsize=(8, 6))
pos = nx.spring_layout(G)  # Positioning the nodes
plt.subplots_adjust(bottom=0.2)  # Adjust the plot to make room for the button

# Colors to track which nodes and edges have been visited and backtracked
node_colors = {node: 'lightblue' for node in G.nodes()}
edge_colors = {edge: 'gray' for edge in G.edges()}

# Function to reset the graph colors before each loop
def reset_graph():
    global node_colors, edge_colors
    node_colors = {node: 'lightblue' for node in G.nodes()}
    edge_colors = {edge: 'gray' for edge in G.edges()}

# Animation function
def update(num):
    if num == 0:
        reset_graph()  # Reset the graph to initial state at the start of the loop

    ax.clear()

    # Draw the full graph structure
    nx.draw(G, pos, ax=ax, node_color=[node_colors[node] for node in G.nodes()], with_labels=True, node_size=500, edge_color=[edge_colors[edge] for edge in G.edges()], width=2)

    # Handle visiting nodes or backtracking
    current_node, action = traversal_order[num]

    if action == 'visit':
        # Mark node as visited (green)
        node_colors[current_node] = 'green'

        # Highlight the edge from the parent to the current node
        if parent[current_node] is not None:
            edge_colors[(parent[current_node], current_node) if (parent[current_node], current_node) in G.edges() else (current_node, parent[current_node])] = 'green'
        ax.set_title(f"Visiting node: {current_node}")
    
    elif action == 'backtrack':
        # Mark node as backtracked (gray)
        node_colors[current_node] = 'gray'

        # Set the backtracked edge to gray
        if parent[current_node] is not None:
            edge_colors[(parent[current_node], current_node) if (parent[current_node], current_node) in G.edges() else (current_node, parent[current_node])] = 'gray'
        ax.set_title(f"Backtracking from: {current_node}")

    # Draw the graph with updated node and edge colors
    nx.draw(G, pos, ax=ax, node_color=[node_colors[node] for node in G.nodes()], with_labels=True, node_size=500, edge_color=[edge_colors[edge] for edge in G.edges()], width=2)

    # Display the current preorder and postorder traversal at the bottom of the plot
    preorder_up_to_now = [node for node in preorder if traversal_order.index((node, 'visit')) <= num]
    postorder_up_to_now = [node for node in postorder if traversal_order.index((node, 'backtrack')) <= num]

    # Move the text lower on the canvas by adjusting the transform values
    ax.text(0.05, -0.05, f"Preorder: {preorder_up_to_now}", transform=ax.transAxes, fontsize=12, verticalalignment='bottom', bbox=dict(facecolor='white', alpha=0.5))
    ax.text(0.05, -0.15, f"Postorder: {postorder_up_to_now}", transform=ax.transAxes, fontsize=12, verticalalignment='bottom', bbox=dict(facecolor='white', alpha=0.5))

# Function to restart the animation and reset the graph colors after completion
def restart_animation(event):
    ani.event_source.stop()
    reset_graph()  # Reset node and edge colors
    ani.frame_seq = ani.new_frame_seq()  # Reset the animation
    ani.event_source.start()

# Create animation with a slower speed (2000 ms interval), and set `repeat=True` to loop it
ani = animation.FuncAnimation(fig, update, frames=len(traversal_order), interval=1500, repeat=True)

# Create the Restart button
restart_ax = plt.axes([0.81, 0.05, 0.1, 0.075])
button = Button(restart_ax, 'Restart', color='lightblue', hovercolor='green')
button.on_clicked(restart_animation)

# Display the animation
plt.show()
