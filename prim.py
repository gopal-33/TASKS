import heapq

class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list

    def add_edge(self, u, v, weight):
        """Add an undirected weighted edge."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))

    def prim_mst(self, start):
        """Find the Minimum Spanning Tree (MST) using Prim’s Algorithm."""
        min_heap = [(0, start)]  # (weight, node)
        visited = set()
        mst_weight = 0
        mst_edges = []

        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if node not in visited:
                visited.add(node)
                mst_weight += weight
                if weight != 0:
                    mst_edges.append((weight, node))

                for edge_weight, neighbor in self.graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (edge_weight, neighbor))

        return mst_weight, mst_edges  # Total weight and MST edges

# Example Usage
g = Graph()
edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4), (3, 4, 3)]
for u, v, w in edges:
    g.add_edge(u, v, w)

mst_weight, mst_edges = g.prim_mst(0)
print("MST Total Weight:", mst_weight)
print("MST Edges:", mst_edges)