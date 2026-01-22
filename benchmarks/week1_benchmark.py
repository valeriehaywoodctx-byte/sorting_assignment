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