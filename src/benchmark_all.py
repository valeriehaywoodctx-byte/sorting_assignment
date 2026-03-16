import time
import matplotlib.pyplot as plt
import numpy as np
from fibonacci import Fibonacci
from knapsack import Knapsack
from lcs import LCS

def benchmark_dp():
    print("🚀 Starting Master Benchmark...")
    
    # 1. FIBONACCI BENCHMARK
    fib = Fibonacci()
    ns = [10, 20, 28, 30, 33, 35]
    naive_f, dp_f = [], []

    print("Running Fibonacci...")
    for n in ns:
        # Time Naive
        start = time.time()
        fib.recursive(n)
        naive_f.append(time.time() - start)
        # Time DP
        start = time.time()
        fib.bottom_up(n)
        dp_f.append(time.time() - start)

    # 2. KNAPSACK BENCHMARK
    ks = Knapsack()
    item_counts = [10, 50, 100, 200]
    ks_times = []

    print("Running Knapsack...")
    for count in item_counts:
        w = list(range(1, count + 1))
        v = list(range(1, count + 1))
        cap = count * 2
        start = time.time()
        ks.bottom_up(w, v, cap)
        ks_times.append(time.time() - start)

    # 3. LCS BENCHMARK
    lcs_obj = LCS()
    lengths = [10, 50, 100, 200]
    lcs_times = []

    print("Running LCS...")
    for length in lengths:
        s1 = "A" * length
        s2 = "T" * (length // 2) + "A" * (length // 2)
        start = time.time()
        lcs_obj.bottom_up(s1, s2)
        lcs_times.append(time.time() - start)

    # --- PLOTTING ---
    print("📊 Generating Graphs...")
    
    # Fibonacci Graph (Naive vs DP)
    plt.figure(figsize=(8, 5))
    plt.plot(ns, naive_f, 'r-o', label='Naive Recursion')
    plt.plot(ns, dp_f, 'g-s', label='Dynamic Programming')
    plt.title('Fibonacci: The Cost of Recursion')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('fibonacci_comparison.png')

    # Knapsack & LCS Scalability
    plt.figure(figsize=(8, 5))
    plt.plot(item_counts, ks_times, 'b-^', label='Knapsack (Bottom-Up)')
    plt.plot(lengths, lcs_times, 'm-x', label='LCS (Bottom-Up)')
    plt.title('Scalability of DP Algorithms')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('dp_scalability.png')

    print("✅ Done! Check your folder for 'fibonacci_comparison.png' and 'dp_scalability.png'")

if __name__ == "__main__":
    benchmark_dp()