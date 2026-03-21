import matplotlib.pyplot as plt
import networkx as nx
import math

def visualize_tsp_logic():
    cities = {"A": (0,0), "B": (1,5), "C": (4,1), "D": (3,3), "E": (5,5)}
    nodes = list(cities.keys())
    G = nx.Graph()
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            d = math.dist(cities[nodes[i]], cities[nodes[j]])
            G.add_edge(nodes[i], nodes[j], weight=d)

    mst = nx.minimum_spanning_tree(G)
    pos = cities

    plt.figure(figsize=(12, 5))

    # Subplot 1: The MST
    plt.subplot(1, 2, 1)
    nx.draw(mst, pos, with_labels=True, node_color='lightblue', edge_color='green', width=2)
    plt.title("Step 1: Minimum Spanning Tree\n(Lower Bound on Optimal)")

    # Subplot 2: The TSP Tour
    plt.subplot(1, 2, 2)
    tour = list(nx.dfs_preorder_nodes(mst, source="A"))
    tour_edges = [(tour[i], tour[(i+1)%len(tour)]) for i in range(len(tour))]
    nx.draw(G, pos, with_labels=True, node_color='lightcoral', edgelist=tour_edges, edge_color='red', width=2)
    plt.title("Step 2: Shortcut Tour\n(Guaranteed ≤ 2x Optimal)")

    plt.savefig("tsp_approximation_logic.png")
    print("✓ Saved tsp_approximation_logic.png")

if __name__ == "__main__":
    visualize_tsp_logic()