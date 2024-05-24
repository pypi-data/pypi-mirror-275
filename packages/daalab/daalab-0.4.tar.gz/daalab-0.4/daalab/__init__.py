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
    "zerone": "space complexity: O(nW) and time complexity: O(nW)",
    "fracknap": "space complexity: O(1) and time complexity: O(n log n)",
    "huffman": "space complexity: O(n) and time complexity: O(n log n)",
    "queen1": "space complexity: O(n) and time complexity: O(n!)",
    "queen2": "space complexity: O(n) and time complexity: O(n!)",
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
    "prims": "space complexity: O(V^2) and time complexity: O(V^2)",
    "bellman": "space complexity: O(V) and time complexity: O(VE)"
}


    print("Available functions in the daalab library:")
    for name, description in functions.items():
        print(f"{name}: {description}")





