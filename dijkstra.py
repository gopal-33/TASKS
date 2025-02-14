import heapq

class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list

    def add_edge(self, u, v, weight):
        """Add a directed weighted edge."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        """Find shortest paths from start node using Dijkstra's Algorithm."""
        min_heap = [(0, start)]  # (distance, node)
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)

            # Process each neighbor
            for neighbor, weight in self.graph[current_node]:
                distance = current_dist + weight
                if distance < distances[neighbor]:  # Found a shorter path
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances  # Shortest path distances

# Example Usage
g = Graph()
edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5), (3, 4, 3)]
for u, v, w in edges:
    g.add_edge(u, v, w)

print("Shortest distances from node 0:")
print(g.dijkstra(0))