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
        available_colors = set(range(len(vertices)))  # All colors available initially
        for neighbor in neighbors:
            if neighbor in colors:
                available_colors.discard(colors[neighbor])  # Remove color of neighbor if it's already assigned
        if available_colors:
            colors[vertex] = min(available_colors)  # Assign the minimum available color
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

def matrix_chain_order(p, i, j):
    if i == j:
        return 0

    min_cost = sys.maxsize
    
    for k in range(i, j):
        count = (matrix_chain_order(p, i, k) +
                 matrix_chain_order(p, k + 1, j) +
                 p[i-1] * p[k] * p[j])

        if count < min_cost:
            min_cost = count
    
    return min_cost

n = int(input("Enter the number of matrices: "))
matrix_dims = list(map(int, input("Enter the dimensions of matrices separated by spaces: ").split()))

min_multiplications = matrix_chain_order(matrix_dims, 0, n - 1)

print("Minimum number of multiplications is", min_multiplications)'''
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
    code = '''import sys

def tsp_max_profit(cities, profits, dist):
    n = len(cities)
    num_sets = 2 ** n
    
    dp = [[sys.maxsize] * n for _ in range(num_sets)]
    dp[1][0] = 0  
    
    for mask in range(1, num_sets):
        for u in range(n):
            if mask & (1 << u):  
                for v in range(n):
                    if u != v and mask & (1 << v): 
                        dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + dist[v][u])
    
    min_dist = sys.maxsize
    for u in range(1, n):
        min_dist = min(min_dist, dp[num_sets - 1][u] + dist[u][0])  
    
    return min_dist

cities = ["A", "B", "C", "D"]
profits = [10, 20, 15, 25]


distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

max_profit = tsp_max_profit(cities, profits, distances)
print("Maximum profit:", max_profit)'''
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

