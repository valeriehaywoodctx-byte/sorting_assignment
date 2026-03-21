import collections

def push_relabel(network, source, sink):
    """
    High-performance Max-Flow using the Push-Relabel (Pre-flow Push) method.
    Scales significantly better than Edmonds-Karp for large networks.
    """
    n = len(network.adj)
    height = {node: 0 for node in network.adj}
    excess = {node: 0 for node in network.adj}
    flow = collections.defaultdict(int)
    
    # Initialize: source height is N, push maximum possible flow from source
    height[source] = n
    for v in network.adj[source]:
        cap = network.capacity[(source, v)]
        flow[(source, v)] = cap
        flow[(v, source)] = -cap
        excess[v] = cap
        excess[source] -= cap

    def push(u, v):
        send = min(excess[u], network.capacity[(u, v)] - flow[(u, v)])
        flow[(u, v)] += send
        flow[(v, u)] -= send
        excess[u] -= send
        excess[v] += send

    def relabel(u):
        min_height = float('inf')
        for v in network.adj[u]:
            if network.capacity[(u, v)] - flow[(u, v)] > 0:
                min_height = min(min_height, height[v])
        if min_height != float('inf'):
            height[u] = min_height + 1

    # Main loop: Find nodes with excess flow (excluding source and sink)
    while True:
        active_nodes = [node for node in network.adj 
                        if node != source and node != sink and excess[node] > 0]
        if not active_nodes:
            break
        
        for u in active_nodes:
            pushed = False
            for v in network.adj[u]:
                if network.capacity[(u, v)] - flow[(u, v)] > 0 and height[u] > height[v]:
                    push(u, v)
                    pushed = True
            
            if not pushed:
                relabel(u)

    return excess[sink], flow