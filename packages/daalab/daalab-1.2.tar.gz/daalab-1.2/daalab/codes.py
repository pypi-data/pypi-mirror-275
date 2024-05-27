def print01():
    code = '''def knapsack(weights, values, capacity, n):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] +
                                dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]
    
    return dp[n][capacity], selected_items

n = int(input("num of items: "))
weights = list(map(int, input("weights with spaced: ").split()))
values = list(map(int, input("values with spaces: ").split()))
capacity = int(input("capacity: "))
max_value, selected_items = knapsack(weights, values, capacity, n)
print("Max val:", max_value)
print("Selected items:", selected_items)'''
    print(code)

def print_fk():
    code = '''def fractional_knapsack(item_weights, item_values, max_capacity):
    items = [(item_values[i] / item_weights[i], item_weights[i], item_values[i]) for i in range(len(item_weights))]
    items.sort(reverse=True)
    
    total_value = 0
    remaining_capacity = max_capacity
    
    for value_ratio, weight, value in items:
        if remaining_capacity >= weight:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += value_ratio * remaining_capacity
            break
            
    return total_value

num_items = int(input("Enter the number of items: "))
weights = []
values = []

print("Enter weights and values for each item:")
for i in range(num_items):
    w = int(input(f"Enter weight for item {i + 1}: "))
    v = int(input(f"Enter value for item {i + 1}: "))
    weights.append(w)
    values.append(v)

capacity = int(input("Enter the capacity of the knapsack: "))

max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value that can be obtained:", max_value)'''
    print(code)



def print_huffman():
    code = '''import heapq

class Node:
    def __init__(self, freq, symbol):
        self.freq = freq
        self.symbol = symbol
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_codes(chars, freq):
    pq = []
    for i in range(len(chars)):
        heapq.heappush(pq, Node(freq[i], chars[i]))

    while len(pq) > 1:
        node1 = heapq.heappop(pq)
        node2 = heapq.heappop(pq)
        merged_freq = node1.freq + node2.freq
        merged_node = Node(merged_freq, None)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(pq, merged_node)

    root = pq[0]
    codes = {}
    build_codes(root, "", codes)
    return codes

def build_codes(node, code, codes):
    if node.symbol:
        codes[node.symbol] = code
    else:
        build_codes(node.left, code + "0", codes)
        build_codes(node.right, code + "1", codes)

chars = input("Enter characters separated by spaces: ").split()
freq = list(map(int, input("Enter corresponding frequencies separated by spaces: ").split()))

codes = huffman_codes(chars, freq)
print("Huffman Codes:")
for char, code in codes.items():
    print(f"{char}: {code}")'''
    print(code)


def print_queen1():
    code = '''def solve_n_queens(n):
    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if all(board[i] != col and board[i] - i != col - row and board[i] + i != col + row for i in range(row)):
                board[row] = col
                solve(board, row + 1)

    solutions = []
    solve([-1] * n, 0)
    return solutions

n = 4
solutions = solve_n_queens(n)
for sol in solutions:
    print(sol)'''
    print(code)


def print_queen2():
    code = '''def is_safe(board, row, col):
    # vertical up
    for i in range(row - 1, -1, -1):
        if board[i][col] == 'Q':
            return False

    # diagonal left up
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # diagonal right up
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def n_queens(board, row):
    # base case
    if row == len(board):
        print_board(board)
        return

    # column loop
    for j in range(len(board)):
        if is_safe(board, row, j):
            board[row][j] = 'Q'
            n_queens(board, row + 1)  # function call
            board[row][j] = 'x'  # backtracking

def print_board(board):
    print("------chess board------")
    for row in board:
        print(" ".join(row))
    print()

n = int(input())
board = [['x' for _ in range(n)] for _ in range(n)]
n_queens(board, 0)'''
    print(code)

def print_graph_colour():
    code = '''class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def get_vertices(self):
        return list(self.graph.keys())

    def get_neighbors(self, vertex):
        return self.graph[vertex]

def graph_coloring(graph):
    colors = {}
    vertices = graph.get_vertices()
    for vertex in vertices:
        neighbors = graph.get_neighbors(vertex)
        available_colors = set(range(len(vertices))) 
        for neighbor in neighbors:
            if neighbor in colors:
                available_colors.discard(colors[neighbor])  
        if available_colors:
            colors[vertex] = min(available_colors) 
        else:
            raise ValueError("No available colors for vertex: " + str(vertex))
    return colors

def main():
    graph = Graph()
    
    num_edges = int(input("Enter the number of edges: "))
    print("Enter edges (e.g., 'u v' for an edge between u and v):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    try:
        coloring = graph_coloring(graph)
        print("Graph coloring:")
        for vertex, color in coloring.items():
            print("Vertex:", vertex, "Color:", color)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()'''
    print(code)


def print_matrixchain():
    code = '''import sys
from typing import List

def matrix_chain_order(p: List[int], n: int) -> tuple[List[List[int]], List[List[int]]]:
    """
    Compute the minimum number of scalar multiplications needed to compute the matrix
    chain product A[i]A[i+1]...A[j] and the optimal order of multiplication.

    Args:
        p (List[int]): List of dimensions of the matrices.
        n (int): Number of matrices.

    Returns:
        Tuple[List[List[int]], List[List[int]]]: m and s matrices, where m[i][j] stores the minimum
        number of scalar multiplications needed to compute the matrix chain product A[i]A[i+1]...A[j],
        and s[i][j] stores the index of the optimal split point in the subproblem.
    """
    m = [[0 for x in range(n)] for y in range(n)]
    s = [[0 for x in range(n)] for y in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            m[i][j] = sys.maxsize

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_order(s: List[List[int]], i: int, j: int) -> None:
    """
    Print the optimal order of matrix multiplication for A[i]A[i+1]...A[j].

    Args:
        s (List[List[int]]): The s matrix computed by matrix_chain_order function.
        i (int): Start index of the matrix chain.
        j (int): End index of the matrix chain.
    """
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_order(s, i, s[i][j])
        print_optimal_order(s, s[i][j] + 1, j)
        print(")", end="")

# Input number of matrices
n = int(input("Enter the number of matrices: ")) + 1

# Input the dimensions of matrices
matrix_dims = list(map(int, input("Enter the dimensions of matrices separated by spaces: ").split()))

# Get the order and the minimum number of multiplications
m, s = matrix_chain_order(matrix_dims, n)

print("Minimum number of multiplications is", m[1][n - 1])
print("Optimal order of multiplication is: ", end="")
print_optimal_order(s, 1, n - 1)
print()


mcm code'''
    print(code)


def print_tspbb():
    code = '''# Python3 program to solve
# Traveling Salesman Problem using
# Branch and Bound.
import math
maxsize = float('inf')

def copyToFinal(curr_path):
	final_path[:N + 1] = curr_path[:]
	final_path[N] = curr_path[0]

def firstMin(adj, i):
	min = maxsize
	for k in range(N):
		if adj[i][k] < min and i != k:
			min = adj[i][k]

	return min

def secondMin(adj, i):
	first, second = maxsize, maxsize
	for j in range(N):
		if i == j:
			continue
		if adj[i][j] <= first:
			second = first
			first = adj[i][j]

		elif(adj[i][j] <= second and
			adj[i][j] != first):
			second = adj[i][j]

	return second

def TSPRec(adj, curr_bound, curr_weight,
			level, curr_path, visited):
	global final_res

	if level == N:

		if adj[curr_path[level - 1]][curr_path[0]] != 0:

			curr_res = curr_weight + adj[curr_path[level - 1]]\
										[curr_path[0]]
			if curr_res < final_res:
				copyToFinal(curr_path)
				final_res = curr_res
		return

	for i in range(N):

		if (adj[curr_path[level-1]][i] != 0 and
							visited[i] == False):
			temp = curr_bound
			curr_weight += adj[curr_path[level - 1]][i]

			if level == 1:
				curr_bound -= ((firstMin(adj, curr_path[level - 1]) +
								firstMin(adj, i)) / 2)
			else:
				curr_bound -= ((secondMin(adj, curr_path[level - 1]) +
								firstMin(adj, i)) / 2)

			if curr_bound + curr_weight < final_res:
				curr_path[level] = i
				visited[i] = True

				TSPRec(adj, curr_bound, curr_weight,
					level + 1, curr_path, visited)

			curr_weight -= adj[curr_path[level - 1]][i]
			curr_bound = temp

			visited = [False] * len(visited)
			for j in range(level):
				if curr_path[j] != -1:
					visited[curr_path[j]] = True

def TSP(adj):

	curr_bound = 0
	curr_path = [-1] * (N + 1)
	visited = [False] * N

	for i in range(N):
		curr_bound += (firstMin(adj, i) +
					secondMin(adj, i))

	curr_bound = math.ceil(curr_bound / 2)

	visited[0] = True
	curr_path[0] = 0

	TSPRec(adj, curr_bound, 0, 1, curr_path, visited)

# Dynamic input for the adjacency matrix
N = int(input("Enter the number of cities: "))
adj = []
print("Enter the adjacency matrix (0 for no edge):")
for i in range(N):
    row = []
    for j in range(N):
        weight = int(input(f"Enter the weight of the edge from city {i} to city {j}: "))
        row.append(weight)
    adj.append(row)

final_path = [None] * (N + 1)

visited = [False] * N

final_res = maxsize

TSP(adj)

print("Minimum cost :", final_res)
print("Path Taken : ", end = ' ')
for i in range(N + 1):
	print(final_path[i], end = ' ')'''
    print(code)

def print_lcs():
    code = '''def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_len = dp[m][n]

    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str = X[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_str, lcs_len

X = input("Enter the first string: ")
Y = input("Enter the second string: ")

lcs_str, lcs_len = lcs(X, Y)
print(f"The length of the longest common subsequence is: {lcs_len}")
print(f"The longest common subsequence is: {lcs_str}")'''
    print(code)


def print_01bb():
    code = '''class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def knapsack_bb(items, capacity):
    def bound(node, weight, value):
        if weight >= capacity:
            return value

        bound_value = value
        for item in items[node:]:
            if weight + item.weight <= capacity:
                bound_value = max(bound_value, value + item.value)

        return bound_value

    def branch_and_bound(node, weight, value, max_value):
        nonlocal best_value, best_items

        if weight <= capacity:
            if value > max_value:
                max_value = value

            if node == len(items):
                if value > best_value:
                    best_value = value
                    best_items = items_taken[:]
                return max_value

            bound_value = bound(node, weight, value)
            if bound_value > best_value:
                items_taken.append(items[node])
                max_value = branch_and_bound(node + 1, weight + items[node].weight, value + items[node].value, max_value)
                items_taken.pop()

                max_value = branch_and_bound(node + 1, weight, value, max_value)

        return max_value

    best_value = 0
    best_items = []
    items_taken = []
    max_value = branch_and_bound(0, 0, 0, 0)

    return best_value, best_items

# Example usage
items = []
for i in range(int(input("Enter number of items: "))):
    weight = int(input("Enter Weight: "))
    value = int(input("Enter Value: "))
    items.append(Item(weight, value))

capacity = int(input("Enter the max capacity of the knapsack: "))

value, items_taken = knapsack_bb(items, capacity)
print(f'Maximum value: {value}')
print(f'Items taken: {[item.value for item in items_taken]}')'''
    print(code)

def print_floyed():
    code = '''INF = 99999999

n = int(input("Enter number of vertices "))
g = []

for i in range(n):
    t = []
    for j in range(n):
        if i != j:
            weight = int(input(f"Enter the weight between the nodes (Enter -1 for no path) {i} and {j} "))
            if weight != -1:
                t.append(weight)
            else:
                t.append(INF)
        else:
            t.append(0)
    g.append(t)



def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)



def print_solution(distance):
    for i in range(n):
        for j in range(n):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

print_solution(g)'''
    print(code)


def print_jobseq():
    code = '''class Job:
    def __init__(self, name, deadline, profit):
        self.name = name
        self.deadline = deadline
        self.profit = profit


def sequence(names, deadlines, profits):
    jobs = [Job(i, j, k) for i, j, k in zip(names, deadlines, profits)]
    jobs.sort(key=lambda x: x.profit, reverse=True)

    maxtime = max(deadlines)
    result = [False] * maxtime
    outjob = ["-1"] * maxtime

    for job in jobs:
        for j in range(min(maxtime - 1, job.deadline - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                outjob[j] = job.name
                break
    return outjob


# names = ['a', 'b', 'c', 'd', 'e']
# deadlines = [2, 1, 2, 1, 3]
# profits = [100, 19, 27, 25, 15]

num_jobs = int(input("Enter the number of jobs: "))
print("Enter the names, deadlines, and profits as space-separated arrays:")
names = input("Names: ").split()
deadlines = list(map(int, input("Deadlines: ").split()))
profits = list(map(int, input("Profits: ").split()))

job = sequence(names, deadlines, profits)

print("The sequence of jobs to be executed is:")
print(job)


job seqencing'''
    print(code)

def print_tspdp():
    code = '''def tsp(graph, start):
    n = len(graph)
    max_distance = float('inf')
    memo = {}
    shortest_path = []

    def dfs(node, visited, path):
        if visited == (1 << n) - 1:
            path.append(start)
            return graph[node][start], path.copy()
        
        if (node, visited) in memo:
            return memo[(node, visited)]

        min_distance = max_distance
        optimal_path = []

        for next_node in range(n):
            if not visited & (1 << next_node):
                distance, temp_path = dfs(next_node, visited | (1 << next_node), path + [next_node])
                distance += graph[node][next_node]
                
                if distance < min_distance:
                    min_distance = distance
                    optimal_path = temp_path

        memo[(node, visited)] = (min_distance, optimal_path)
        return min_distance, optimal_path

    distance, path = dfs(start, 1 << start, [start])

    return distance, path


n = int(input("Enter the number of cities: "))

print("Enter the distances between cities (use space-separated values):")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start_node = int(input("Enter the start city (0-indexed): "))

print("\nDistances between cities:")
for row in graph:
    print(row)

distance, path = tsp(graph, start_node)

print("\nMinimum distance for TSP:", distance)
print("Optimal path:", path)'''
    print(code)


def print_kruskal():
    code = '''class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Minimum Spanning Tree:")
        for u, v, weight in result:
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

    graph.kruskal_mst()


if __name__ == "__main__":
    main()'''
    print(code)

def print_dijkstra():
    code = '''class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min = 1e7

        for v in range(self.V):
            if dist[v] < min and sptSet[v] is False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] is False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


n = int(input("Enter matrix size: "))
D = [[]] * n
for i in range(n):
    D[i] = list(map(int, input("Enter row: ").split()))
source = int(input("Enter source: "))

g = Graph(n)
g.graph = D
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]]
g.dijkstra(source)'''
    print(code)


def print_prims():
    code = '''import heapq

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
    main()'''
    print(code)


def print_bellman():
    code = '''def bellman_ford(graph, source):
    # Step 1: Initialize distances
    distances = {vertex: float("inf") for vertex in graph}
    distances[source] = 0

    # Step 2: Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # Step 3: Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains negative weight cycle")

    return distances


# Example
# graph = {"A": {"B": -1, "C": 4}, "B": {"C": 3, "D": 2, "E": 2}, "C": {}, "D": {"B": 1, "C": 5}, "E": {"D": -3}}
# source = "A"
graph = {}
while True:
    edge = input("Enter source, dest, cost - ")
    if edge.strip() == "":
        break
    temp = edge.split()
    if len(temp) == 3:
        u, v, w = temp
    elif len(temp) == 1:
        graph[temp[0]] = {}
    w = int(w)
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = w
print(graph)
source = input("enter source - ")

shortest_distances = bellman_ford(graph, source)
print(shortest_distances)'''
    print(code)


def print_huffman2():
    code = '''option = input("Enter 'string' if you want to enter a string or 'freq' if you want to enter frequencies - ")
if option=='string':
    string = input('Enter string')
elif option == 'freq':
    n = int(input('Enter number of letters - '))
    string=''
    for i in range(n):
        letter, freq = input('Enter letter and frequency space-separated - ').split()
        string+= letter*int(freq)
    
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def __str__(self):
        return "%s_%s" % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=""):
    if isinstance(node, str):
        return {node: binString}
    left, right = node.children()
    d = dict()
    d.update(huffman_code_tree(left, True, binString + "0"))
    d.update(huffman_code_tree(right, False, binString + "1"))
    return d


freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(" Char | Huffman code ")
print("----------------------")
for char, frequency in freq:
    print(" %-4r |%12s" % (char, huffmanCode[char]))'''
    print(code)


def print_graphcol2():
    code = '''class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def get_vertices(self):
        return list(self.graph.keys())

    def get_neighbors(self, vertex):
        return self.graph[vertex]

def graph_coloring_backtracking(graph):
    def is_safe(node, color, coloring):
        for neighbor in graph.get_neighbors(node):
            if coloring[neighbor] == color:
                return False
        return True

    def solve(node, coloring, colors_used):
        nonlocal min_colors_used
        if node == len(vertices):
            min_colors_used = min(min_colors_used, colors_used)
            return

        for color in range(1, colors_used + 2):
            if is_safe(vertices[node], color, coloring):
                coloring[vertices[node]] = color
                solve(node + 1, coloring, max(colors_used, color))
                coloring[vertices[node]] = 0

    vertices = graph.get_vertices()
    coloring = {vertex: 0 for vertex in vertices}
    min_colors_used = float('inf')

    for vertex in vertices:
        coloring[vertex] = 1
        solve(1, coloring, 1)
        coloring[vertex] = 0

    return min_colors_used, coloring

def main():
    graph = Graph()

    print("Enter edges (e.g., 'u v' for an edge between u and v):")
    num_edges = int(input("Enter number of edges: "))

    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    try:
        min_colors_used, coloring = graph_coloring_backtracking(graph)
        print("Graph coloring:")
        for vertex, color in coloring.items():
            if color != 0:
                print("Vertex:", vertex, "Color:", color)
        print("Chromatic number:", min_colors_used)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()'''
    print(code)



def print_react_form():
    code = '''import React, { useState } from 'react';

const FormComponent = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: ''
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Submitted Data:\nName: ${formData.name}\nEmail: ${formData.email}\nPassword: ${formData.password}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
        />
      </div>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
        />
      </div>
      <div>
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default FormComponent;
'''
    print(code)



def print_react_timetable():
    code = '''import React from 'react';

const Timetable = () => {
  return (
    <div className="container mt-4">
      <h3 className="text-center mb-4">CHAITANYA BHARATHI INSTITUTE OF TECHNOLOGY </h3>
      <h3 className="text-center mb-4">DEPARTMENT OF COMPUTER ENGINEERING AND TECHNOLOGY</h3>
      <h4 className="text-center mb-4">Class Time Table for the AY 2023-24    VI - Semester</h4>
      <h4 className="text-center mb-4">Class B.E - VI Semester           W.E.F.: 12-02-2024           Room No. A-301</h4>
      <table className="table table-bordered text-center">
        <thead className="thead-dark">
          <tr className='theaad'>
            <th >
            <div className="trow">
                Period
              </div>
              <div className="trow">
                Day/ Time
              </div>
            </th>
            <th>
            <div className="trow">
                I
              </div>
              <div className="trow">
              9:00 AM - 10:00 AM
              </div>
              </th>
            <th>
            <div className="trow">
                II
              </div>
              <div className="trow">
              10:10 AM - 11:10 AM
              </div>
              </th>
            <th>
            <div className="trow">
                III
              </div>
              <div className="trow">
              11:20 AM - 12:20 PM
              </div></th>
            <th className='luncho'>
            12:20 PM - 1:10 PM</th>
            <th>
            <div className="trow">
                IV
              </div>
              <div className="trow">
              1:10 PM - 2:10 PM
              </div></th>
            <th>
            <div className="trow">
                V
              </div>
              <div className="trow">
              2:20 PM - 3:20 PM
              </div></th>
            <th>
            <div className="trow">
                VI
              </div>
              <div className="trow">
              3:30 PM - 4:30 PM
              </div></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className='greyed'>MONDAY</td>
            <td>P.E II SC</td>
            <td>SE</td>
            <td>BPA</td>
            <td className='lunch' rowSpan="6" style={{ writingMode: 'vertical-rl', textAlign: 'center', verticalAlign: 'middle' }}>LUNCH</td>
            <td colSpan="3">BPA Lab @ TPO-1</td>
            
          </tr>
          <tr>
            <td className='greyed'>TUESDAY</td>
            
            <td>TOC</td>
            <td colSpan="2">
              <div className="trow">
                UML Lab B2 @Lab -9
              </div>
              <div className="trow">
                ES Lab B-1
              </div>
            </td>
            <td>SE</td>
            <td>PE-II SC @ A302, VAPT @A-301</td>
            <td>UHV</td>
          </tr>
          <tr>
            <td className='greyed'>WEDNESDAY</td>
            <td>BPA</td>
            <td>PE-II SCO Lab-9,VAPT@A-301</td>
            <td>TOC</td>
            <td>OE-II TWS@ A-301 FN @ Lab 9</td>
            <td>UHV</td>
            <td>SPORTS</td>
          </tr>
          <tr>
            <td className='greyed'>THURSDAY</td>
            <td>TOC</td>
            <td>SE</td>
            <td>LIBRARY</td>
            <td>PE-II SC @ Lab-9, VAPT @A-301</td>
            <td>BPA</td>
            <td>OE TWS @ A-301, FM @A-302</td>
          </tr>
          <tr>
            <td className='greyed'>FRIDAY</td>
            <td>UHV</td>
            <td>SE</td>
            <td>OE TWS @ A-301, FM @A-302</td>
            <td>MENTORING</td>
            <td colSpan="2"><div className="trow">
                UML Lab B1 @Lab -9
              </div>
              <div className="trow">
                ES Lab B-2
              </div></td>
          </tr>
          <tr>
            <td className='greyed'>SATURDAY</td>
            <td colSpan="2"><div className="trow">
            PE-II:VAPT LAB ® TPO-3
              </div>
              <div className="trow">
              PE-II:SC LAB ® Lab - 10
              </div></td>
            <td>BPA</td>
            <td>TOC</td>
            <td>OE-II TWS @ A-301</td>
            <td></td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default Timetable;
'''
    print(code)


def print_react_sp():
    code = '''import React from 'react';
import ChildComponent from './ChildComponent';

const ParentComponent = () => {
  const parentData = "Data from Parent Component";

  return (
    <div>
      <h1>Parent Component</h1>
      <ChildComponent data={parentData} />
    </div>
  );
};

export default ParentComponent;



import React, { useState } from 'react';

const ChildComponent = ({ data }) => {
  const [childData, setChildData] = useState("Initial Child Data");

  const updateChildData = () => {
    setChildData("Updated Child Data");
  };

  return (
    <div>
      <h2>Child Component</h2>
      <p>{data}</p>
      <p>{childData}</p>
      <button onClick={updateChildData}>Update Child Data</button>
    </div>
  );
};

export default ChildComponent;
'''
    print(code)

def print_react_func():
    code = '''import React from 'react';

const FunctionalComponent = () => {
  return (
    <div>
      <h1>Hello, I am a Functional Component!</h1>
    </div>
  );
};

export default FunctionalComponent;



import React, { Component } from 'react';

class ClassComponent extends Component {
  render() {
    return (
      <div>
        <h1>Hello, I am a Class Component!</h1>
      </div>
    );
  }
}

export default ClassComponent;
'''
    print(code)

def print_react_routes():
    code = '''
//in this you will have to create the form.jsx and timetable.jsx or some other components 
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Timetable from './Timetable';
import Form from './Form';
import Home from './Home';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/timetable" element={<Timetable />} />
          <Route path="/form" element={<Form />} />
          <Route path="/" element={<Home/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;


//home.jsx:
import React from 'react'
import { useNavigate } from 'react-router-dom'

const Home = () => {
    const navigate = useNavigate();

    const handleclicktimetable = (()=>{
        navigate('/timetable')
    })

    const handleclickform = (()=>{
        navigate('/form')
    })

  return (
    <div className='home'>
        <div className="button" onClick={handleclicktimetable}>
            Open Timetable
        </div>
        <div className="button " onClick={handleclickform}>
            Open Form
        </div>
    </div>
  )
}

export default Home
'''
    print(code)


def print_react_es5_es6():
    code = '''// ES5 Version

// Function to calculate factorial using traditional function declaration
function factorialES5(num) {
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorialES5(num - 1);
  }
}

// Using the function to calculate factorial of 5
console.log(factorialES5(5)); // Output: 120


// ES6 Version

// Function to calculate factorial using arrow function
const factorialES6 = (num) => {
  return (num === 0 || num === 1) ? 1 : num * factorialES6(num - 1);
}

// Using the function to calculate factorial of 5
console.log(factorialES6(5)); // Output: 120'''
    print(code)

def print_form_validation():
    code = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Form Validation on Button Click</title>
</head>
<body>
<form id="myForm" onsubmit="return validateForm()">
    <label for="username">Username:</label>
    <input type="text" id="username">
    <br>

    <label for="password">Password:</label>
    <input type="password" id="password">
    <br>

    <label for="email">Email:</label>
    <input type="email" id="email">
    <br>

    <button type="submit">Submit</button>
</form>

<script>
function validateForm() {
    event.preventDefault(); // Prevent form from submitting

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var email = document.getElementById('email').value;

    var usernameRegex = /^[a-zA-Z0-9]{3,16}$/;
    var passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$/;
    var emailRegex = /^[a-zA-Z0-9.%+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (!usernameRegex.test(username)) {
        alert('Enter a valid username.');
        return false;
    }

    if (!passwordRegex.test(password)) {
        alert('Enter a valid password.');
        return false;
    }

    if (!emailRegex.test(email)) {
        alert('Enter a valid email address.');
        return false;
    }

    return true; // Only returns true if all validations pass
}
</script>
</body>
</html>
'''
    print(code)

def print_bootstrap_table():
    code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Enhanced Bootstrap Table</title>
    <!-- Link to Bootstrap CSS for styling -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-3">
        <h2>Feature-Rich Bootstrap Table</h2>
        <!-- Table Responsive Wrapper -->
        <div class="table-responsive">
            <!-- Table with striped rows, hover effect, and bordered layout -->
            <table class="table table-striped table-hover table-bordered">
                <!-- Dark table header -->
                <thead class="table-dark">
                    <tr>
                        <th>#</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>City</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>John</td>
                        <td>Doe</td>
                        <td>john@example.com</td>
                        <td>New York</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>Jane</td>
                        <td>Doe</td>
                        <td>jane@example.com</td>
                        <td>Los Angeles</td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>Jim</td>
                        <td>Beam</td>
                        <td>jim@example.com</td>
                        <td>Chicago</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
'''
    print(code)


def print_crud():
    code = '''
mongo
use myDatabase
db.myCollection.insertOne({ name: "John", age: 30 })

db.myCollection.findOne({ name: "John" })


db.myCollection.updateOne({ name: "John" }, { $set: { age: 31 } })


db.myCollection.findOne({ name: "John" })


db.myCollection.deleteOne({ name: "John" })
'''
    print(code)