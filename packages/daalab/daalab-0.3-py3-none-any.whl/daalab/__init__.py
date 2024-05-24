from .codes import print01, print_fk, print_huffman, print_queen1, print_queen2, print_graph_colour, print_matrixchain, print_tspbb, print_lcs, print_01bb, print_floyed, print_tspdp, print_jobseq, print_dijkstra, print_kruskal, print_prims, print_bellman

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


def list():
    functions = {
        "zerone": "Prints the code for the 0/1 Knapsack problem",
        "fracknap": "Prints the code for the Fractional Knapsack problem",
        "huffman": "Prints the code for Huffman Coding",
        "queen1": "Prints the code for the N-Queens problem (Method 1)",
        "queen2": "Prints the code for the N-Queens problem (Method 2)",
        "graphcol": "Prints the code for Graph Coloring",
        "matrixchain": "Prints the code for Matrix Chain Multiplication",
        "tspbb": "Prints the code for the Traveling Salesman Problem (Branch and Bound)",
        "lcs": "Prints the code for Longest Common Subsequence",
        "zeronebb": "Prints the code for the 0/1 Knapsack problem (Branch and Bound)",
        "floyed": "Prints the code for Floyd-Warshall algorithm",
        "tspdp": "Prints the code for the Traveling Salesman Problem (Dynamic Programming)",
        "jobseq": "Prints the code for Job Sequencing with Deadlines",
        "dijkstra": "Prints the code for Dijkstra's algorithm",
        "kruskal": "Prints the code for Kruskal's algorithm",
        "prims": "Prints the code for Prims's algorithm",
        "bellman": "Prints the code for Bellman's algorithm"
    }

    print("Available functions in the daalab library:")
    for name, description in functions.items():
        print(f"{name}: {description}")





