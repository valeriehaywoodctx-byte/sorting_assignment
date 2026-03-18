import networkx as nx
import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def tsp_mst_doubling(cities):
    """
    2-Approximation for Metric TSP.
    Logic: Find MST -> DFS Traverse (Shortcut) -> Return to Start.
    """
    G = nx.Graph()
    nodes = list(cities.keys())
    
    # Create a complete graph with distances as weights
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            d = distance(cities[nodes[i]], cities[nodes[j]])
            G.add_edge(nodes[i], nodes[j], weight=d)
    
    # 1. Compute Minimum Spanning Tree
    mst = nx.minimum_spanning_tree(G)
    
    # 2. Perform DFS traversal to get a tour (Shortcutting visited nodes)
    tour_nodes = list(nx.dfs_preorder_nodes(mst, source=nodes[0]))
    
    # 3. Calculate total distance
    total_dist = 0
    for i in range(len(tour_nodes)):
        u = tour_nodes[i]
        v = tour_nodes[(i + 1) % len(tour_nodes)]
        total_dist += distance(cities[u], cities[v])
        
    tour_nodes.append(nodes[0]) # Close the loop
    return tour_nodes, total_dist

if __name__ == "__main__":
    test_cities = {"A": (0,0), "B": (1,5), "C": (4,1), "D": (3,3)}
    path, dist = tsp_mst_doubling(test_cities)
    print(f"MST-Doubling Tour: {' -> '.join(path)}")
    print(f"Total Distance: {dist:.2f}")