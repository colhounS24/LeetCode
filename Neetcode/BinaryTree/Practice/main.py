# DFS

# Define the decision tree as a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}


def dfs_recursive(tree, node, visited=None): # Takes in a tree,node, and optionally a visited Node - that defaults to None
    # Base case. make a set called visited - for O(1) lookup
    if visited is None:
        visited = set()  # Initialize the visited set
    visited.add(node)    # Mark the node as visited
    print(node)          # Print the current node (for illustration)
    for child in tree[node]:  # Recursively visit children
        if child not in visited:
            dfs_recursive(tree, child, visited)

# Run DFS starting from node 'A'
#dfs_recursive(tree, 'A')


# BFS

from collections import deque

def bfs(start, tree):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in tree[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

#bfs("A", tree)

