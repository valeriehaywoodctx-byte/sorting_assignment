import matplotlib.pyplot as plt

def visualize_rounding():
    subsets = ["Set 1", "Set 2", "Set 3", "Set 4"]
    lp_values = [0.15, 0.85, 0.45, 0.95] # Mock values similar to your output
    rounded_values = [0, 1, 0, 1]

    plt.figure(figsize=(10, 6))
    plt.bar(subsets, lp_values, alpha=0.5, label="LP Fractional Value (Relaxed)", color='blue')
    plt.step(subsets, rounded_values, where='mid', label="Binary Decision (Rounded)", color='red', linewidth=2)
    
    plt.axhline(y=0.5, color='gray', linestyle='--', label="Rounding Threshold (0.5)")
    plt.title("Set Cover: LP Relaxation vs. Deterministic Rounding")
    plt.ylabel("Selection Strength (0 to 1)")
    plt.legend()
    plt.savefig("lp_rounding_viz.png")
    print("✓ Saved lp_rounding_viz.png")

if __name__ == "__main__":
    visualize_rounding()