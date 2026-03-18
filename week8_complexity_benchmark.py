import time
import matplotlib.pyplot as plt
import random
from src.complexity.subset_sum_backtracking import subset_sum_backtracking

def benchmark_complexity():
    # We will test sizes from 5 to 25. 
    # Warning: Going much higher than 25 might take a very long time!
    sizes = list(range(5, 26, 2)) 
    runtimes = []

    print("Starting Exponential Growth Benchmark...")
    for n in sizes:
        # Create a random set of n numbers
        numbers = [random.randint(1, 100) for _ in range(n)]
        target = random.randint(50, 200)
        
        start_time = time.time()
        subset_sum_backtracking(numbers, target)
        end_time = time.time()
        
        elapsed = end_time - start_time
        runtimes.append(elapsed)
        print(f"n={n:2d} | Time: {elapsed:.6f}s")

    # Plotting the "Exponential Wall"
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, runtimes, marker='o', color='red', label='Backtracking O(2^n)')
    plt.title('The Exponential Wall: Subset Sum Complexity')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.grid(True)
    plt.legend()
    plt.savefig('complexity_explosion.png')
    print("\n✓ Saved complexity_explosion.png")

if __name__ == "__main__":
    benchmark_complexity()