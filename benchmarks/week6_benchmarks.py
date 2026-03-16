import matplotlib.pyplot as plt

def run_accurate_benchmark():
    capacities = [100, 500, 1000, 2500, 5000]
    items = 100
    byte_size = 8 # 64-bit integer
    
    std_mem = []
    opt_mem = []

    print(f"{'W':<10} | {'2D Table (KB)':<15} | {'1D Table (KB)':<15} | {'Reduction'}")
    print("-" * 60)

    for W in capacities:
        # Standard: (N+1) * (W+1) * 8 bytes
        m2d = ((items + 1) * (W + 1) * byte_size) / 1024
        # Optimized: (W+1) * 8 bytes
        m1d = ((W + 1) * byte_size) / 1024
        
        reduction = ((m2d - m1d) / m2d) * 100
        std_mem.append(m2d)
        opt_mem.append(m1d)
        
        print(f"{W:<10} | {m2d:<15.2f} | {m1d:<15.2f} | {reduction:.1f}%")

    plt.figure(figsize=(10, 6))
    plt.plot(capacities, std_mem, 'r-o', label='Standard 2D DP (KB)')
    plt.plot(capacities, opt_mem, 'g-s', label='Optimized 1D DP (KB)')
    plt.title('Memory Scaling: 2D vs 1D Knapsack')
    plt.xlabel('Knapsack Capacity (W)')
    plt.ylabel('Memory Usage (Kilobytes)')
    plt.legend()
    plt.grid(True)
    plt.savefig('knapsack_final_graph.png')
    print("\n✅ New graph 'knapsack_final_graph.png' created.")

if __name__ == "__main__":
    run_accurate_benchmark()