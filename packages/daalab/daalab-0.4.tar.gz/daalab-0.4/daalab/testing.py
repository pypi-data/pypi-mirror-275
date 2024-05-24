import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        mst = []  # Result array to store the MST edges
        visited = [False] * self.V  # Array to keep track of visited vertices
        min_heap = [(0, 0)]  # Min-heap to select the edge with the smallest weight

        while min_heap:
            weight, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True

            for v, w in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
                    mst.append((u, v, w))

        print("Minimum Spanning Tree:")
        for u, v, weight in mst:
            print(f"{u} -- {v} == {weight}")

# Example usage
def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))
    graph = Graph(vertices)

    print("Enter edges as 'source destination weight':")
    for _ in range(edges):
        u, v, w = map(int, input().split())
        graph.add_edge(u, v, w)

    graph.prim_mst()

if __name__ == "__main__":
    main()