<<<<<<< HEAD
import sys
import os

# This tells Python to look in the main folder for the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import random
from src.sorting.basic_sorts import bubble_sort, selection_sort, insertion_sort
import random
from src.sorting.basic_sorts import bubble_sort, selection_sort, insertion_sort

def _time_sort(sort_func, data):
    start = time.perf_counter()
    sort_func(data)
    return time.perf_counter() - start

def run_benchmark(size: int, repeats: int = 5):
    print(f"--- Timing {size} elements ({repeats} repeats) ---")
    sort_funcs = [bubble_sort, selection_sort, insertion_sort]
    totals = {f.__name__: 0.0 for f in sort_funcs}

    for _ in range(repeats):
        base = [random.randint(0, 1000) for _ in range(size)]
        for f in sort_funcs:
            data = base.copy()  # ensure each algorithm sees the same input
            totals[f.__name__] += _time_sort(f, data)

    for f in sort_funcs:
        avg = totals[f.__name__] / repeats
        print(f"{f.__name__:<15}: {avg:.5f} seconds (avg)")
    print("")

if __name__ == "__main__":
    run_benchmark(500, repeats=3)
    run_benchmark(1000, repeats=2)
=======
import sys
import os
import time
import random
import pandas as pd
import matplotlib.pyplot as plt  # <--- NEW: This is the "drawing" tool

# This tells Python to look in the main folder for the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sorting.basic_sorts import bubble_sort, selection_sort, insertion_sort

def _time_sort(sort_func, data):
    start = time.perf_counter()
    sort_func(data)
    return time.perf_counter() - start

def run_benchmark():
    sizes = [100, 500, 1000, 5000, 10000]
    repeats = 3
    sort_funcs = [bubble_sort, selection_sort, insertion_sort]
    all_results = []

    for size in sizes:
        print(f"--- Timing {size} elements ({repeats} repeats) ---")
        totals = {f.__name__: 0.0 for f in sort_funcs}

        for _ in range(repeats):
            base = [random.randint(0, 1000) for _ in range(size)]
            for f in sort_funcs:
                data = base.copy()
                totals[f.__name__] += _time_sort(f, data)

        for f in sort_funcs:
            avg = totals[f.__name__] / repeats
            print(f"{f.__name__:<15}: {avg:.5f} seconds (avg)")
            all_results.append({
                "Algorithm": f.__name__,
                "Size": size,
                "AverageTime": avg
            })

    # --- SAVE TO CSV ---
    df = pd.DataFrame(all_results)
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_dir = os.path.join(root_dir, "benchmarks", "results")
    os.makedirs(output_dir, exist_ok=True)
    
    csv_path = os.path.join(output_dir, "sorting_results.csv")
    df.to_csv(csv_path, index=False)
    print(f"\n✅ Data saved to: {csv_path}")

    # --- NEW: CREATE THE GRAPH ---
    plt.figure(figsize=(10, 6))
    for algo in df['Algorithm'].unique():
        subset = df[df['Algorithm'] == algo]
        plt.plot(subset['Size'], subset['AverageTime'], label=algo, marker='o')

    plt.title('Sorting Algorithm Performance')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (Seconds)')
    plt.legend()
    plt.grid(True)
    
    chart_path = os.path.join(output_dir, "sorting_chart.png")
    plt.savefig(chart_path)
    print(f"📈 Graph saved to: {chart_path}")

# This is the "Start" button for the whole script
if __name__ == "__main__":
    run_benchmark()
>>>>>>> f9a8675 (Final submission for Week 2 with all folders)
