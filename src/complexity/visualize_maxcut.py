import matplotlib.pyplot as plt
from src.complexity.maxcut_randomized import randomized_max_cut

def visualize_maxcut_prob():
    nodes = range(20)
    edges = [(random.randint(0,19), random.randint(0,19)) for _ in range(50)]
    results = []

    for _ in range(1000):
        _, _, count = randomized_max_cut(nodes, edges)
        results.append(count)

    plt.figure(figsize=(10, 6))
    plt.hist(results, bins=15, color='purple', edgecolor='black')
    plt.axvline(25, color='yellow', linestyle='dashed', linewidth=2, label="Expectation (|E|/2)")
    plt.title("Distribution of 1,000 Randomized Max-Cut Trials")
    plt.xlabel("Number of Edges Cut")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig("maxcut_distribution.png")
    print("✓ Saved maxcut_distribution.png")

import random
if __name__ == "__main__":
    visualize_maxcut_prob()