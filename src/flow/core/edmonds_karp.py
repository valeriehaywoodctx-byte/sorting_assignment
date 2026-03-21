from collections import deque

def edmonds_karp(network, source, sink):
    """
    Finds the Maximum Flow using BFS to find augmenting paths.
    """
    parent = {}
    max_flow = 0
    flow = collections.defaultdict(int)

    def bfs():
        """Finds an augmenting path using BFS."""
        visited = {source}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in network.adj[u]:
                # If there's residual capacity and we haven't visited v
                if v not in visited and network.capacity[(u, v)] - flow[(u, v)] > 0:
                    parent[v] = u
                    visited.add(v)
                    if v == sink:
                        return True
                    queue.append(v)
        return False

    # Keep augmenting while a path exists
    while bfs():
        path_flow = float('inf')
        s = sink
        
        # Find the bottleneck (smallest capacity) in the path
        while s != source:
            path_flow = min(path_flow, network.capacity[(parent[s], s)] - flow[(parent[s], s)])
            s = parent[s]

        # Update flow and residual edges
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            flow[(u, v)] += path_flow
            flow[(v, u)] -= path_flow # The 'back-flow' logic
            v = parent[v]
            
        parent = {} # Reset for next BFS

    return max_flow, flow

import collections