import collections

def min_cost_max_flow(network, source, sink):
    """
    Finds the Max Flow that has the Minimum total Cost.
    Uses the Successive Shortest Path algorithm with SPFA.
    """
    flow = collections.defaultdict(int)
    total_flow = 0
    total_cost = 0

    while True:
        # Find shortest path based on COST (not distance)
        dist = {node: float('inf') for node in network.adj}
        parent = {node: None for node in network.adj}
        dist[source] = 0
        
        # SPFA (Shortest Path Faster Algorithm) to find the cheapest augmenting path
        queue = collections.deque([source])
        in_queue = {node: False for node in network.adj}
        in_queue[source] = True
        
        while queue:
            u = queue.popleft()
            in_queue[u] = False
            for v in network.adj[u]:
                # Only look at edges with remaining capacity
                if network.capacity[(u, v)] - flow[(u, v)] > 0:
                    if dist[v] > dist[u] + network.cost[(u, v)]:
                        dist[v] = dist[u] + network.cost[(u, v)]
                        parent[v] = u
                        if not in_queue[v]:
                            queue.append(v)
                            in_queue[v] = True
        
        # If the sink is unreachable, we've found the Max Flow
        if dist[sink] == float('inf'):
            break

        # Find the bottleneck capacity along this cheapest path
        path_flow = float('inf')
        curr = sink
        while curr != source:
            prev = parent[curr]
            path_flow = min(path_flow, network.capacity[(prev, curr)] - flow[(prev, curr)])
            curr = prev
        
        # Update flow and accumulate total cost
        total_flow += path_flow
        curr = sink
        while curr != source:
            prev = parent[curr]
            flow[(prev, curr)] += path_flow
            flow[(curr, prev)] -= path_flow  # Residual back-edge
            total_cost += path_flow * network.cost[(prev, curr)]
            curr = prev

    return total_flow, total_cost, flow