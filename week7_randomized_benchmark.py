import time
import random
import matplotlib.pyplot as plt
import numpy as np
from src.randomized.randomized_quicksort import randomized_quicksort
from src.randomized.bloom_filter import BloomFilter
from src.randomized.minhash_similarity import jaccard_similarity, minhash_signature, estimate_similarity

# Helper: Deterministic QuickSort (Simplified for comparison)
def deterministic_quicksort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quicksort(left) + middle + deterministic_quicksort(right)

def benchmark_quicksort():
    sizes = [100, 500, 1000, 5000, 10000]
    rand_times = []
    det_times = []

    for n in sizes:
        # Create a 'Worst Case' scenario (already sorted array)
        test_data = list(range(n))
        
        # Test Deterministic
        start = time.time()
        deterministic_quicksort(test_data.copy())
        det_times.append(time.time() - start)

        # Test Randomized
        start = time.time()
        randomized_quicksort(test_data.copy(), 0, n - 1)
        rand_times.append(time.time() - start)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, det_times, label='Deterministic (Sorted Input)', marker='o')
    plt.plot(sizes, rand_times, label='Randomized (Sorted Input)', marker='s')
    plt.title('QuickSort: Deterministic vs Randomized (Worst Case)')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('quicksort_comparison.png')
    print("✓ Saved quicksort_comparison.png")

def benchmark_bloom_filter():
    bf = BloomFilter(size=5000, hash_count=5)
    items_added = [f"user_{i}" for i in range(1000)]
    for item in items_added: bf.add(item)

    false_positives = 0
    test_items = [f"stranger_{i}" for i in range(1000)]
    for item in test_items:
        if bf.check(item):
            false_positives += 1
    
    print(f"✓ Bloom Filter False Positive Rate: {false_positives/1000:.4f}")

if __name__ == "__main__":
    print("Starting Week 7 Benchmarks...")
    benchmark_quicksort()
    benchmark_bloom_filter()
    print("All benchmarks complete!")