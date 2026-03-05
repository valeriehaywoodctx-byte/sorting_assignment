import time
import random
from src.sorting.merge_sort import merge_sort
from src.sorting.quick_sort import quick_sort

def generate_test_data(size, data_type):
    """Generates the specific data scenarios required for the technical report."""
    if data_type == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reverse":
        return list(range(size, 0, -1))
    elif data_type == "nearly_sorted":
        data = list(range(size))
        # 95% sorted: swap 5% of elements
        for _ in range(int(size * 0.05)):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            data[i], data[j] = data[j], data[i]
        return data
    elif data_type == "many_duplicates":
        # Only 10 unique values
        return [random.randint(1, 10) for _ in range(size)]
    return []

def run_suite():
    # Recommended sizes for your 1200-word report
    sizes = [100, 500, 1000, 5000, 10000]
    data_types = ["random", "sorted", "reverse", "nearly_sorted", "many_duplicates"]
    
    print(f"{'Algorithm':<12} | {'Data Type':<15} | {'Size':<6} | {'Time (s)'}")
    print("-" * 55)

    for size in sizes:
        for d_type in data_types:
            original_data = generate_test_data(size, d_type)
            
            for name, func in [("Merge", merge_sort), ("Quick", quick_sort)]:
                # Use a copy to ensure we don't modify the data for the next algorithm
                data_copy = original_data[:]
                
                start = time.perf_counter()
                func(data_copy)
                end = time.perf_counter()
                
                print(f"{name:<12} | {d_type:<15} | {size:<6} | {end - start:.6f}")

if __name__ == "__main__":
    run_suite()