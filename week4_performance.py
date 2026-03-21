import time
from src.graphs.graph import Graph
from src.graphs.bfs import bfs

def benchmark_graphs():
    size = 1000  # Increased size for better data
    print(f"--- Benchmarking Graph with {size} nodes ---")

    # Adjacency List
    g_list = Graph(directed=False, use_matrix=False)
    for i in range(size):
        g_list.add_edge(i, (i + 1) % size)
    
    start_time = time.time()
    for _ in range(10):  # Run 10 times to get an average
        bfs(g_list, 0)
    print(f"Adjacency List BFS (Avg of 10): {(time.time() - start_time) / 10:.6f}s")

    # Adjacency Matrix
    g_matrix = Graph(directed=False, use_matrix=True)
    for i in range(size):
        g_matrix.add_edge(i, (i + 1) % size)
    
    start_time = time.time()
    for _ in range(10):
        bfs(g_matrix, 0)
    print(f"Adjacency Matrix BFS (Avg of 10): {(time.time() - start_time) / 10:.6f}s")

if __name__ == "__main__":
    benchmark_graphs()