import matplotlib.pyplot as plt
import time
import random
from src.complexity.tsp_metric_approx import tsp_mst_doubling
from src.complexity.maxcut_randomized import randomized_max_cut

def run_benchmarks():
    sizes = [5, 10, 20, 50, 100]
    tsp_times = []
    maxcut_times = []
    
    print("Starting Week 9 Approximation Benchmarks...")
    
    for n in sizes:
        # Benchmark TSP
        cities = {f"C{i}": (random.uniform(0, 100), random.uniform(0, 100)) for i in range(n)}
        start = time.time()
        tsp_mst_doubling(cities)
        tsp_times.append(time.time() - start)
        
        # Benchmark Max-Cut
        nodes = list(range(n))
        # Create a random graph with density 0.3
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < 0.3:
                    edges.append((i, j))
        
        start = time.time()
        randomized_max_cut(nodes, edges)
        maxcut_times.append(time.time() - start)
        print(f"n={n} | TSP: {tsp_times[-1]:.4f}s | Max-Cut: {maxcut_times[-1]:.4f}s")

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, tsp_times, marker='o', label='MST-Doubling TSP (O(n²))')
    plt.plot(sizes, maxcut_times, marker='s', label='Randomized Max-Cut (O(n+m))')
    plt.title("Scalability of Approximation Algorithms")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.savefig("approx_scalability.png")
    print("\n✓ Saved approx_scalability.png")

if __name__ == "__main__":
    run_benchmarks()