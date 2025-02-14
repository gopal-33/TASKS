class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list

    def add_edge(self, u, v):
        """Add an edge to the graph (undirected)."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, visited=None):
        """Recursive DFS traversal."""
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")  # Process the node

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def dfs_iterative(self, start):
        """Iterative DFS using a stack."""
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                stack.extend(reversed(self.graph[node]))  # Reverse to maintain order

# Example Usage
g = Graph()
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
for u, v in edges:
    g.add_edge(u, v)

print("Recursive DFS:")
g.dfs(0)

print("\nIterative DFS:")
g.dfs_iterative(0)