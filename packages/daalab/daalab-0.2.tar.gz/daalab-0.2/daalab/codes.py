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