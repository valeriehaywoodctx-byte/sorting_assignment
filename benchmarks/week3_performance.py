import time
import random
from src.sorting.heap import MinHeap

def benchmark_heap(sizes):
    print(f"{'Size':<10} | {'Insert Time (s)':<15}")
    print("-" * 30)
    
    for size in sizes:
        data = [random.randint(1, 100000) for _ in range(size)]
        heap = MinHeap()
        
        start_time = time.time()
        for item in data:
            heap.insert(item)
        end_time = time.time()
        
        print(f"{size:<10} | {end_time - start_time:<15.6f}")

if __name__ == "__main__":
    test_sizes = [1000, 5000, 10000, 50000]
    benchmark_heap(test_sizes)