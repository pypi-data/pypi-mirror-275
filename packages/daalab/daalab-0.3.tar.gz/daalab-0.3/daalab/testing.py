def list_functions():
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
        "kruskal": "Prints the code for Kruskal's algorithm"
    }

    print("Available functions in the daalab library:")
    for name, description in functions.items():
        print(f"{name}: {description}")

list_functions()