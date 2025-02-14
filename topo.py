from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)

    def add_edge(self, u, v):
        """Add a directed edge (u -> v)."""
        self.graph[u].append(v)
        self.in_degree[v] += 1
        if u not in self.in_degree:
            self.in_degree[u] = 0  # Ensure all nodes are tracked

    def topological_sort(self):
        """Perform Topological Sort using Kahn's Algorithm."""
        queue = deque([node for node in self.in_degree if self.in_degree[node] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for neighbor in self.graph[node]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) != len(self.in_degree):
            print("Cycle detected! Topological sorting not possible.")
            return []

        return topo_order

# Example Usage
g = Graph()
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
for u, v in edges:
    g.add_edge(u, v)

print("Topological Order:", g.topological_sort())
