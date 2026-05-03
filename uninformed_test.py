import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from id_dfs import iddfs

# Graph definition - CORRECT VERSION
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Create directed graph
G = nx.DiGraph()

# Add edges
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)

nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True
)

plt.title("Graph Representation")
plt.show()

# Function calls
print("BFS:", bfs(graph, 'A'))
print("DFS:", dfs(graph, 'A'))
print("IDDFS:", iddfs(graph, 'A', 4))