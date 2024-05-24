from .codes import print01, print_fk, print_huffman, print_queen1, print_queen2, print_graph_colour, print_matrixchain, print_tspbb, print_lcs, print_01bb, print_floyed, print_tspdp, print_jobseq, print_dijkstra, print_kruskal, print_prims, print_bellman, print_huffman2

zerone = print01
fracknap = print_fk
huffman = print_huffman
queen1 = print_queen1
queen2 = print_queen2
graphcol = print_graph_colour
matrixchain = print_matrixchain
tspbb = print_tspbb
lcs = print_lcs
zeronebb = print_01bb
floyed = print_floyed
tspdp = print_tspdp
jobseq = print_jobseq
dijkstra = print_dijkstra
kruskal = print_kruskal
prims = print_prims
bellman = print_bellman
huffman2 = print_huffman2


def list():
    functions = {
    "zerone": "space complexity: O(nW) and time complexity: O(nW)",
    "fracknap": "space complexity: O(n) and time complexity: O(n log n)",
    "huffman": "space complexity: O(n) and time complexity: O(n log n)",
    "queen1": "space complexity: O(n) and time complexity: O(n!)",
    "queen2": "space complexity: O(n^2) and time complexity: O(n!)",
    "graphcol": "space complexity: O(V) and time complexity: O(V+E)",
    "matrixchain": "space complexity: O(n^2) and time complexity: O(n^3)",
    "tspbb": "space complexity: O(n^2) and time complexity: O(n^2 * 2^n)",
    "lcs": "space complexity: O(mn) and time complexity: O(mn)",
    "zeronebb": "space complexity: O(n) and time complexity: O(2^n)",
    "floyed": "space complexity: O(n^2) and time complexity: O(n^3)",
    "tspdp": "space complexity: O(n * 2^n) and time complexity: O(n^2 * 2^n)",
    "jobseq": "space complexity: O(n) and time complexity: O(n log n)",
    "dijkstra": "space complexity: O(V^2) and time complexity: O(V^2)",
    "kruskal": "space complexity: O(E) and time complexity: O(E log V)",
    "prims": "space complexity: O(V+E) and time complexity: O(E logV)",
    "bellman": "space complexity: O(V) and time complexity: O(VE)"
}


    print("Available functions in the daalab library:")
    for name, description in functions.items():
        print(f"{name}: {description}")

def viva():
    questions='''### Dynamic Programming Viva Questions

1. **What is Dynamic Programming (DP)?**
   - Dynamic Programming is a method for solving complex problems by breaking them down into simpler subproblems. It is applicable when the problem can be divided into overlapping subproblems that can be solved independently.

2. **Explain the two main approaches to Dynamic Programming.**
   - The two main approaches are:
     1. Top-Down (Memoization): Solving the problem recursively and storing the results of subproblems to avoid redundant computations.
     2. Bottom-Up (Tabulation): Solving the subproblems iteratively and storing their results in a table.

3. **What is the principle of optimality in Dynamic Programming?**
   - The principle of optimality states that the optimal solution to a problem can be constructed from optimal solutions to its subproblems.

4. **How does Dynamic Programming differ from Divide and Conquer?**
   - Dynamic Programming solves subproblems once and stores their solutions, while Divide and Conquer may solve the same subproblem multiple times without storing the results.

5. **Give an example of a problem that can be solved using Dynamic Programming.**
   - Examples include the Fibonacci sequence, Longest Common Subsequence (LCS), and the Knapsack problem.

6. **What is memoization?**
   - Memoization is a technique where the results of expensive function calls are cached and reused to avoid redundant computations in a top-down approach.

7. **Explain the concept of overlapping subproblems.**
   - Overlapping subproblems refer to subproblems that recur multiple times in the recursive solution of a problem, making DP an efficient approach.

8. **Describe the difference between memoization and tabulation.**
   - Memoization is a top-down approach that stores results of subproblems during recursion, while tabulation is a bottom-up approach that iteratively solves subproblems and stores their results in a table.

9. **What is the Longest Common Subsequence (LCS) problem?**
   - The LCS problem is about finding the longest subsequence present in two sequences that appears in the same order in both sequences.

10. **How is the Knapsack problem solved using Dynamic Programming?**
    - The Knapsack problem is solved by building a DP table where each entry represents the maximum value that can be achieved with a given weight capacity and subset of items.

### Zero/One Knapsack Problem

1. **Explain the 0/1 Knapsack problem.**
   - It is a problem where we need to maximize the total value of items that can be put into a knapsack of fixed capacity, with each item being either included or excluded (0/1 decision).

2. **What is the time complexity of the DP solution for the 0/1 Knapsack problem?**
   - The time complexity is O(nW), where n is the number of items and W is the capacity of the knapsack.

3. **What does each cell in the DP table represent in the 0/1 Knapsack problem?**
   - Each cell represents the maximum value that can be achieved with a given weight capacity and subset of items.

4. **Can the 0/1 Knapsack problem be solved using a greedy algorithm?**
   - No, the 0/1 Knapsack problem cannot be solved using a greedy algorithm because it may not yield the optimal solution.

5. **How is the DP table initialized in the 0/1 Knapsack problem?**
   - The first row and first column are initialized to 0, representing zero items or zero capacity.

6. **What is the difference between the 0/1 Knapsack and the fractional Knapsack problem?**
   - In the 0/1 Knapsack problem, items cannot be divided, whereas in the fractional Knapsack problem, items can be broken into smaller pieces.

7. **What is the recurrence relation used in the DP solution of the 0/1 Knapsack problem?**
   - \( DP[i][w] = \max(DP[i-1][w], DP[i-1][w - weight[i-1]] + value[i-1]) \)

8. **Why is the 0/1 Knapsack problem classified as NP-complete?**
   - Because there is no known polynomial-time solution for all instances of the problem.

9. **What are some real-life applications of the 0/1 Knapsack problem?**
   - Resource allocation, budget management, and load balancing.

10. **How can you optimize the space complexity of the 0/1 Knapsack problem?**
    - By using a 1D array instead of a 2D array, updating values in place from right to left.

### Fractional Knapsack Problem

1. **What is the fractional Knapsack problem?**
   - It is a problem where we need to maximize the total value of items that can be put into a knapsack, and items can be divided into smaller parts.

2. **How is the fractional Knapsack problem solved?**
   - Using a greedy algorithm that selects items based on the highest value-to-weight ratio.

3. **What is the time complexity of the fractional Knapsack problem solution?**
   - O(n log n), due to the sorting step based on value-to-weight ratios.

4. **Can the fractional Knapsack problem be solved using Dynamic Programming?**
   - It can be solved using Dynamic Programming, but a greedy approach is more efficient.

5. **What is the main difference between the 0/1 Knapsack and the fractional Knapsack problem?**
   - In the 0/1 Knapsack problem, items cannot be split, while in the fractional Knapsack problem, they can.

6. **Explain the greedy choice property in the context of the fractional Knapsack problem.**
   - The greedy choice property means selecting the item with the highest value-to-weight ratio first to maximize the total value.

7. **What does the optimal substructure property imply in the fractional Knapsack problem?**
   - The optimal solution to the problem can be constructed from optimal solutions to subproblems.

8. **Why is the fractional Knapsack problem not NP-complete?**
   - Because it can be solved in polynomial time using a greedy algorithm.

9. **What real-world scenarios can be modeled using the fractional Knapsack problem?**
   - Investment decisions, resource allocation where resources can be split.

10. **How do you handle items that cannot be split in the fractional Knapsack problem?**
    - If items cannot be split, it becomes a 0/1 Knapsack problem.

### Huffman Coding

1. **What is Huffman Coding?**
   - Huffman Coding is a lossless data compression algorithm that assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters.

2. **How is the Huffman tree constructed?**
   - By repeatedly merging the two least frequent nodes until only one node remains.

3. **What is the time complexity of building a Huffman tree?**
   - O(n log n), where n is the number of unique characters.

4. **Explain the concept of prefix-free codes in Huffman Coding.**
   - In prefix-free codes, no code is a prefix of another, ensuring that the code is uniquely decodable.

5. **How does Huffman Coding ensure optimality?**
   - By assigning shorter codes to more frequent characters, minimizing the total encoded length.

6. **What is a min-heap and how is it used in Huffman Coding?**
   - A min-heap is a binary heap where the root node is the smallest element. It is used to efficiently extract the two least frequent nodes during tree construction.

7. **Describe the process of encoding a message using Huffman Coding.**
   - Convert the message characters to their corresponding Huffman codes based on the constructed tree.

8. **What is the difference between fixed-length and variable-length coding?**
   - Fixed-length coding assigns the same number of bits to each character, while variable-length coding assigns different numbers of bits based on frequency.

9. **What are some applications of Huffman Coding?**
   - File compression formats (e.g., ZIP, JPEG), multimedia codecs, and network data transmission.

10. **How is the Huffman tree used for decoding a message?**
    - By traversing the tree from the root to the leaves based on the encoded bits until a leaf node (character) is reached.

### Job Sequencing Problem

1. **What is the Job Sequencing problem?**
   - It is a problem where we aim to maximize profit by scheduling jobs to be completed within their deadlines.

2. **What is the greedy algorithm used for Job Sequencing?**
   - Jobs are sorted in decreasing order of profit and scheduled in the latest available slot before their deadline.

3. **What is the time complexity of the greedy algorithm for Job Sequencing?**
   - O(n log n) due to the sorting step.

4. **How do you handle jobs with deadlines longer than the number of jobs?**
   - Treat the problem as having a maximum deadline equal to the number of jobs.

5. **What is a feasible schedule in the Job Sequencing problem?**
   - A schedule where each job is completed within its deadline.

6. **Explain how disjoint-set data structures can be used in Job Sequencing.**
   - Disjoint-set data structures can help efficiently find and union available slots for scheduling jobs.

7. **What are some real-life applications of the Job Sequencing problem?**
   - Project scheduling, manufacturing processes, and deadline-based service assignments.

8. **What is the difference between weighted and unweighted Job Sequencing problems?**
   - In weighted problems, jobs have associated profits, while in unweighted problems, the goal is to maximize the number of completed jobs.

9. **How do you handle jobs with overlapping deadlines

 in the Job Sequencing problem?**
   - By scheduling the most profitable jobs first within the available time slots.

10. **Can Dynamic Programming be used to solve the Job Sequencing problem?**
    - Yes, Dynamic Programming can be used, but a greedy approach is usually more efficient.

### Graph Colouring Problem

1. **What is the Graph Colouring problem?**
   - It is a problem of assigning colors to the vertices of a graph such that no two adjacent vertices share the same color.

2. **What is the chromatic number of a graph?**
   - The minimum number of colors needed to color the graph.

3. **What is a valid coloring in the context of Graph Colouring?**
   - A coloring where no two adjacent vertices have the same color.

4. **Explain the greedy algorithm for Graph Colouring.**
   - Assign colors to vertices one by one, choosing the smallest available color that has not been used by adjacent vertices.

5. **What is the time complexity of the greedy Graph Colouring algorithm?**
   - O(V^2 + E), where V is the number of vertices and E is the number of edges.

6. **What is a bipartite graph and how is it related to Graph Colouring?**
   - A bipartite graph can be colored with two colors, as its vertices can be divided into two disjoint sets with no edges within each set.

7. **Can the Graph Colouring problem be solved using Dynamic Programming?**
   - Dynamic Programming can be used for specific cases, but it is generally NP-complete.

8. **What are some applications of Graph Colouring?**
   - Scheduling problems, register allocation in compilers, and frequency assignment in wireless networks.

9. **What is the significance of the four-color theorem in Graph Colouring?**
   - It states that any planar graph can be colored with at most four colors.

10. **How do you handle weighted Graph Colouring problems?**
    - By considering additional constraints and optimizing the coloring based on the weights.

### Matrix Chain Multiplication

1. **What is the Matrix Chain Multiplication problem?**
   - It is a problem of determining the optimal order of multiplying a given sequence of matrices to minimize the total number of scalar multiplications.

2. **What is the key idea behind the Dynamic Programming solution to Matrix Chain Multiplication?**
   - To break the problem into subproblems and use a table to store the minimum number of multiplications needed for each subproblem.

3. **What does each entry in the DP table represent in the Matrix Chain Multiplication problem?**
   - Each entry \( DP[i][j] \) represents the minimum number of scalar multiplications needed to multiply matrices from \( i \) to \( j \).

4. **What is the time complexity of the Dynamic Programming solution for Matrix Chain Multiplication?**
   - O(n^3), where n is the number of matrices.

5. **How is the DP table initialized in the Matrix Chain Multiplication problem?**
   - The diagonal entries are initialized to 0, representing a single matrix that requires no multiplication.

6. **What is the recurrence relation used in the DP solution of Matrix Chain Multiplication?**
   - \( DP[i][j] = \min_{k=i}^{j-1} (DP[i][k] + DP[k+1][j] + p_{i-1} \cdot p_k \cdot p_j) \)

7. **Can the Matrix Chain Multiplication problem be solved using a greedy algorithm?**
   - No, a greedy algorithm does not guarantee the optimal solution for this problem.

8. **What are some applications of Matrix Chain Multiplication?**
   - Optimizing matrix operations in computer graphics, scientific computing, and database query optimization.

9. **Explain the concept of parenthesization in Matrix Chain Multiplication.**
   - Parenthesization determines the order in which matrices are multiplied to minimize the number of scalar multiplications.

10. **How do you retrieve the optimal parenthesization from the DP table in Matrix Chain Multiplication?**
    - By using a separate table to store the split points and tracing back from the final solution.

### Travelling Salesman Problem (Branch and Bound)

1. **What is the Travelling Salesman Problem (TSP)?**
   - The TSP is a problem where a salesman must visit a set of cities exactly once and return to the starting city, with the goal of minimizing the total travel distance.

2. **What is the Branch and Bound approach for solving the TSP?**
   - Branch and Bound is an optimization technique that systematically explores all possible routes, pruning routes that exceed the current best solution.

3. **What is the significance of the lower bound in the Branch and Bound approach?**
   - The lower bound helps in pruning branches that cannot yield a better solution than the current best.

4. **What are the key components of a Branch and Bound algorithm?**
   - Branching, bounding, and pruning.

5. **How does the Branch and Bound approach differ from Dynamic Programming for the TSP?**
   - Branch and Bound explores potential solutions in a tree-like structure, while Dynamic Programming solves subproblems and uses their solutions.

6. **What is the time complexity of the Branch and Bound approach for TSP?**
   - The worst-case time complexity is O(n!), but pruning significantly reduces the actual computation time.

7. **What is a heuristic and how is it used in the Branch and Bound approach for TSP?**
   - A heuristic provides a quick, non-optimal solution to guide the search process and improve pruning efficiency.

8. **What are some real-life applications of the TSP?**
   - Logistics, route planning, and circuit design.

9. **How do you handle asymmetric TSP using the Branch and Bound approach?**
   - By considering the direction-specific costs in the bounding function.

10. **What is the difference between symmetric and asymmetric TSP?**
    - In symmetric TSP, the distance between two cities is the same in both directions, while in asymmetric TSP, the distances can differ.

### Longest Common Subsequence (LCS)

1. **What is the Longest Common Subsequence (LCS) problem?**
   - It is a problem of finding the longest subsequence common to two sequences, where the subsequence appears in the same order in both sequences but not necessarily consecutively.

2. **What is the Dynamic Programming approach to solving the LCS problem?**
   - By constructing a DP table where each entry \( DP[i][j] \) represents the length of the LCS of the first \( i \) characters of one sequence and the first \( j \) characters of the other.

3. **What is the time complexity of the DP solution for the LCS problem?**
   - O(mn), where m and n are the lengths of the two sequences.

4. **What does each entry in the DP table represent in the LCS problem?**
   - The length of the LCS of the prefixes of the two sequences up to the current indices.

5. **What is the recurrence relation used in the DP solution of the LCS problem?**
   - \( DP[i][j] = DP[i-1][j-1] + 1 \) if \( X[i-1] = Y[j-1] \), otherwise \( DP[i][j] = \max(DP[i-1][j], DP[i][j-1]) \).

6. **How do you retrieve the actual LCS from the DP table?**
   - By tracing back from \( DP[m][n] \) to \( DP[0][0] \) using the relationships defined in the recurrence.

7. **Can the LCS problem be solved using a greedy algorithm?**
   - No, a greedy algorithm does not guarantee the optimal solution for the LCS problem.

8. **What are some applications of the LCS problem?**
   - Bioinformatics (DNA sequence alignment), text comparison, and version control systems.

9. **How is the DP table initialized in the LCS problem?**
   - The first row and first column are initialized to 0, representing an empty subsequence comparison.

10. **What is the difference between the LCS problem and the Longest Common Substring problem?**
    - The LCS problem allows for non-consecutive subsequences, while the Longest Common Substring problem requires the subsequence to be contiguous.

### Floyd-Warshall Algorithm

1. **What is the Floyd-Warshall algorithm used for?**
   - It is used to find the shortest paths between all pairs of vertices in a weighted graph.

2. **What is the time complexity of the Floyd-Warshall algorithm?**
   - O(V^3), where V is the number of vertices in the graph.

3. **What type of graphs can the Floyd-Warshall algorithm be applied to?**
   - It can be applied to both directed and undirected graphs, including graphs with negative edge weights but no negative weight cycles.

4. **How is the DP table initialized in the Floyd-Warshall algorithm?**
   - The DP table is initialized with direct edge weights, and \( DP[i][i] \) is set to 0 for all vertices \( i \).

5. **What is the main idea behind the Floyd-Warshall algorithm?**
   - To iteratively improve the shortest paths by considering all pairs of vertices and checking if a shorter path exists through an intermediate vertex.

6. **Explain the recurrence relation used in the Floyd-Warshall algorithm.**
   - \( DP[i][j] = \min(DP[i][j], DP[i][k] + DP[k][j]) \) for all vertices \( k \).

7. **What are some applications of the Floyd-Warshall algorithm

?**
   - Network routing, finding transitive closure of graphs, and all-pairs shortest path problems.

8. **How does the Floyd-Warshall algorithm handle negative weight cycles?**
   - It does not handle them directly, but the presence of negative weight cycles can be detected if \( DP[i][i] \) becomes negative for any vertex \( i \).

9. **What is the space complexity of the Floyd-Warshall algorithm?**
   - O(V^2), due to the DP table storing shortest path distances between all pairs of vertices.

10. **Can the Floyd-Warshall algorithm be used for unweighted graphs?**
    - Yes, it can be used for unweighted graphs, but simpler algorithms like BFS may be more efficient in such cases.

### Travelling Salesman Problem (Dynamic Programming)

1. **What is the Dynamic Programming approach to solving the TSP?**
   - The Dynamic Programming approach involves using a DP table to store the shortest paths for subsets of cities and solving the problem in a bottom-up manner.

2. **What is the state representation in the DP solution for the TSP?**
   - The state is represented as \( DP[mask][i] \), where \( mask \) is a bitmask representing the set of visited cities, and \( i \) is the current city.

3. **What is the recurrence relation used in the DP solution for the TSP?**
   - \( DP[mask][i] = \min(DP[mask \setminus (1 << i)][j] + cost[j][i]) \) for all \( j \) in \( mask \).

4. **What is the time complexity of the DP solution for the TSP?**
   - O(n^2 * 2^n), where n is the number of cities.

5. **What are the initial conditions in the DP table for the TSP?**
   - \( DP[1 << i][i] = cost[0][i] \) for all cities \( i \), representing direct travel from the starting city.

6. **How do you reconstruct the optimal tour from the DP table in the TSP?**
   - By tracing back from the final state \( DP[2^n - 1][0] \) using the stored transitions.

7. **What are some limitations of the DP solution for the TSP?**
   - The exponential time complexity limits its applicability to small instances.

8. **Can heuristics be used to improve the DP solution for the TSP?**
   - Yes, heuristics can provide good initial solutions to guide the DP approach.

9. **What is the difference between the DP and Branch and Bound approaches for the TSP?**
   - DP uses a bottom-up approach with a DP table, while Branch and Bound explores the solution space in a tree-like structure.

10. **What are some real-world applications of the TSP?**
    - Route planning, logistics, and manufacturing process optimization.

### Job Sequencing Problem

1. **What is the Job Sequencing problem?**
   - It is a problem where we aim to maximize profit by scheduling jobs to be completed within their deadlines.

2. **What is the greedy algorithm used for Job Sequencing?**
   - Jobs are sorted in decreasing order of profit and scheduled in the latest available slot before their deadline.

3. **What is the time complexity of the greedy algorithm for Job Sequencing?**
   - O(n log n) due to the sorting step.

4. **How do you handle jobs with deadlines longer than the number of jobs?**
   - Treat the problem as having a maximum deadline equal to the number of jobs.

5. **What is a feasible schedule in the Job Sequencing problem?**
   - A schedule where each job is completed within its deadline.

6. **Explain how disjoint-set data structures can be used in Job Sequencing.**
   - Disjoint-set data structures can help efficiently find and union available slots for scheduling jobs.

7. **What are some real-life applications of the Job Sequencing problem?**
   - Project scheduling, manufacturing processes, and deadline-based service assignments.

8. **What is the difference between weighted and unweighted Job Sequencing problems?**
   - In weighted problems, jobs have associated profits, while in unweighted problems, the goal is to maximize the number of completed jobs.

9. **How do you handle jobs with overlapping deadlines in the Job Sequencing problem?**
   - By scheduling the most profitable jobs first within the available time slots.

10. **Can Dynamic Programming be used to solve the Job Sequencing problem?**
    - Yes, Dynamic Programming can be used, but a greedy approach is usually more efficient.

### Dijkstra's Algorithm

1. **What is Dijkstra's algorithm used for?**
   - It is used to find the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights.

2. **What is the time complexity of Dijkstra's algorithm using a min-heap (priority queue)?**
   - O((V + E) log V), where V is the number of vertices and E is the number of edges.

3. **How does Dijkstra's algorithm work?**
   - It starts from the source vertex, repeatedly selects the vertex with the minimum distance, and updates the distances to its adjacent vertices.

4. **Can Dijkstra's algorithm handle graphs with negative edge weights?**
   - No, Dijkstra's algorithm does not work correctly with negative edge weights.

5. **What is the main data structure used in Dijkstra's algorithm?**
   - A priority queue (min-heap) to efficiently select the vertex with the minimum distance.

6. **What are some applications of Dijkstra's algorithm?**
   - Network routing, geographical mapping, and shortest path problems in transportation systems.

7. **How is the distance array initialized in Dijkstra's algorithm?**
   - The distance to the source vertex is set to 0, and all other distances are set to infinity.

8. **What is the difference between Dijkstra's algorithm and the Bellman-Ford algorithm?**
   - Dijkstra's algorithm is faster but cannot handle negative edge weights, while Bellman-Ford can handle negative edge weights and detect negative weight cycles.

9. **How do you reconstruct the shortest path from the distance array in Dijkstra's algorithm?**
   - By maintaining a predecessor array and tracing back from the destination vertex to the source.

10. **What is a practical optimization for Dijkstra's algorithm?**
    - Using a Fibonacci heap instead of a binary heap can improve the time complexity for dense graphs.

### Kruskal's Algorithm

1. **What is Kruskal's algorithm used for?**
   - It is used to find the Minimum Spanning Tree (MST) of a connected, undirected graph.

2. **What is the time complexity of Kruskal's algorithm?**
   - O(E log E), where E is the number of edges, mainly due to the sorting step.

3. **How does Kruskal's algorithm work?**
   - It sorts all edges by weight and adds them to the MST, ensuring no cycles are formed, until the MST includes all vertices.

4. **What data structures are essential for Kruskal's algorithm?**
   - A disjoint-set (union-find) data structure to manage and merge sets of vertices.

5. **Can Kruskal's algorithm handle graphs with negative edge weights?**
   - Yes, it can handle negative edge weights as long as the graph is connected and undirected.

6. **What is the difference between Kruskal's and Prim's algorithms?**
   - Kruskal's algorithm builds the MST by adding edges in increasing order of weight, while Prim's algorithm builds the MST by expanding from a starting vertex.

7. **What are some applications of Kruskal's algorithm?**
   - Network design, clustering algorithms, and constructing efficient road systems.

8. **How is the union-find data structure used in Kruskal's algorithm?**
   - To efficiently check and merge sets of vertices, preventing cycles.

9. **What is a Minimum Spanning Tree (MST)?**
   - An MST is a subset of the edges of a graph that connects all vertices with the minimum possible total edge weight and no cycles.

10. **How do you handle disconnected graphs in Kruskal's algorithm?**
    - Kruskal's algorithm cannot be directly applied to disconnected graphs; each connected component's MST must be found separately.

### Prim's Algorithm

1. **What is Prim's algorithm used for?**
   - It is used to find the Minimum Spanning Tree (MST) of a connected, undirected graph.

2. **What is the time complexity of Prim's algorithm using a min-heap (priority queue)?**
   - O((V + E) log V), where V is the number of vertices and E is the number of edges.

3. **How does Prim's algorithm work?**
   - It starts from an arbitrary vertex and expands the MST by adding the minimum weight edge connecting a vertex inside the MST to a vertex outside the MST.

4. **Can Prim's algorithm handle graphs with negative edge weights?**
   - Yes, it can handle negative edge weights as long as the graph is connected and undirected.

5. **What is the main data structure used in Prim's algorithm?**
   - A priority queue (min-heap) to efficiently select the minimum weight edge.

6. **What are some applications of Prim's algorithm?**
   - Network design, cluster analysis, and creating efficient wiring layouts.

7. **How is the priority queue initialized in Prim's algorithm?**
   - All vertices are initialized with an infinite key value, except the starting vertex, which is set to 0.

8. **What is the difference between Prim

's and Kruskal's algorithms?**
   - Prim's algorithm builds the MST by expanding from a starting vertex, while Kruskal's algorithm builds the MST by adding edges in increasing order of weight.

9. **How do you handle disconnected graphs in Prim's algorithm?**
   - Prim's algorithm cannot be directly applied to disconnected graphs; each connected component's MST must be found separately.

10. **What is a Minimum Spanning Tree (MST)?**
    - An MST is a subset of the edges of a graph that connects all vertices with the minimum possible total edge weight and no cycles.

### Bellman-Ford Algorithm

1. **What is the Bellman-Ford algorithm used for?**
   - It is used to find the shortest path from a single source vertex to all other vertices in a weighted graph and can handle negative edge weights.

2. **What is the time complexity of the Bellman-Ford algorithm?**
   - O(VE), where V is the number of vertices and E is the number of edges.

3. **How does the Bellman-Ford algorithm work?**
   - It iteratively relaxes all edges up to \( V-1 \) times, ensuring the shortest paths are found.

4. **Can the Bellman-Ford algorithm handle graphs with negative weight cycles?**
   - Yes, it can detect negative weight cycles by performing an additional relaxation step.

5. **What are some applications of the Bellman-Ford algorithm?**
   - Network routing, finding shortest paths in graphs with negative weights, and detecting negative weight cycles.

6. **How is the distance array initialized in the Bellman-Ford algorithm?**
   - The distance to the source vertex is set to 0, and all other distances are set to infinity.

7. **What is the difference between the Bellman-Ford and Dijkstra's algorithms?**
   - Bellman-Ford can handle negative edge weights and detect negative weight cycles, while Dijkstra's algorithm is faster but cannot handle negative edge weights.

8. **How do you reconstruct the shortest path from the distance array in the Bellman-Ford algorithm?**
   - By maintaining a predecessor array and tracing back from the destination vertex to the source.

9. **What is the main advantage of the Bellman-Ford algorithm over Dijkstra's algorithm?**
   - Its ability to handle graphs with negative edge weights and detect negative weight cycles.

10. **How do you detect negative weight cycles using the Bellman-Ford algorithm?**
    - By checking for further relaxation in an additional iteration after \( V-1 \) iterations.

### Johnson's Algorithm

1. **What is Johnson's algorithm used for?**
   - It is used to find the shortest paths between all pairs of vertices in a weighted graph, even with negative edge weights.

2. **What is the time complexity of Johnson's algorithm?**
   - O(V^2 log V + VE), where V is the number of vertices and E is the number of edges.

3. **How does Johnson's algorithm work?**
   - It reweights the graph using a potential function derived from the Bellman-Ford algorithm, then applies Dijkstra's algorithm to'''
    print(questions)



