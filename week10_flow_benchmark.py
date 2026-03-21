import time
import random
import matplotlib.pyplot as plt
from src.flow.core.network import FlowNetwork
from src.flow.core.edmonds_karp import edmonds_karp
from src.flow.core.push_relabel import push_relabel

def generate_random_network(n_nodes, n_edges):
    fn = FlowNetwork()
    nodes = [f"n{i}" for i in range(n_nodes)]
    source, sink = nodes[0], nodes[-1]
    
    for _ in range(n_edges):
        u, v = random.sample(nodes, 2)
        cap = random.randint(1, 100)
        fn.add_edge(u, v, cap)
    
    return fn, source, sink

def run_benchmark():
    sizes = [10, 50, 100, 200, 300] # Number of nodes
    ek_times = []
    pr_times = []

    print("Starting Benchmark (this may take a moment)...")
    for n in sizes:
        # Create a graph with edges = nodes * 3
        fn, s, t = generate_random_network(n, n * 3)
        
        # Benchmark Edmonds-Karp
        start = time.time()
        edmonds_karp(fn, s, t)
        ek_times.append(time.time() - start)
        
        # Benchmark Push-Relabel
        start = time.time()
        push_relabel(fn, s, t)
        pr_times.append(time.time() - start)
        print(f"Finished size {n}")

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, ek_times, label='Edmonds-Karp', marker='o')
    plt.plot(sizes, pr_times, label='Push-Relabel', marker='s')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Scaling Analysis: Edmonds-Karp vs. Push-Relabel')
    plt.legend()
    plt.grid(True)
    plt.savefig('flow_scaling.png')
    plt.show()

if __name__ == "__main__":
    run_benchmark()