import timeit
import heapq

def get_report_data():
    sizes = [100, 1000, 10000]
    print("\n--- PERFORMANCE DATA FOR SECTION 3 ---")
    print(f"{'Structure':<15} | {'n=100':<12} | {'n=1000':<12} | {'n=10000':<12}")
    print("-" * 60)

    # 1. Hash Table (Python Dictionary)
    hash_times = []
    for n in sizes:
        t = timeit.timeit(lambda: {i: i for i in range(n)}, number=10) / 10
        hash_times.append(f"{t:.6f}s")
    print(f"{'Hash Table':<15} | {hash_times[0]:<12} | {hash_times[1]:<12} | {hash_times[2]:<12}")

    # 2. Binary Heap (using Python's heapq)
    heap_times = []
    for n in sizes:
        def test_heap():
            h = []
            for i in range(n): heapq.heappush(h, i)
        t = timeit.timeit(test_heap, number=10) / 10
        heap_times.append(f"{t:.6f}s")
    print(f"{'Binary Heap':<15} | {heap_times[0]:<12} | {heap_times[1]:<12} | {heap_times[2]:<12}")

if __name__ == "__main__":
    get_report_data()