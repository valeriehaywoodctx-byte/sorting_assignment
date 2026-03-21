import networkx as nx
import matplotlib.pyplot as plt

def draw_flow_network(network, flow_dict, title="Flow Network Visualization"):
    """
    Draws the graph showing capacity and current flow on each edge.
    Edges are labeled as: current_flow / capacity
    """
    G = nx.DiGraph()
    
    # Add edges that have capacity > 0 (ignore the 0-capacity residual back-edges for the drawing)
    for (u, v), cap in network.capacity.items():
        if cap > 0:
            current_flow = flow_dict.get((u, v), 0)
            G.add_edge(u, v, capacity=cap, flow=current_flow)

    pos = nx.spring_layout(G)  # Position the nodes
    plt.figure(figsize=(10, 7))
    
    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='skyblue', 
            node_size=2000, edge_color='gray', arrowsize=20)
    
    # Create labels: "flow / capacity"
    edge_labels = {(u, v): f"{d['flow']}/{d['capacity']}" 
                   for u, v, d in G.edges(data=True)}
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    
    plt.title(title)
    plt.show()