import collections

class FlowNetwork:
    def __init__(self):
        self.adj = collections.defaultdict(list)
        self.capacity = {}
        self.cost = {}  # New: tracks cost per unit of flow

    def add_edge(self, u, v, cap, cost=0):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.capacity[(u, v)] = cap
        self.capacity[(v, u)] = 0
        self.cost[(u, v)] = cost
        self.cost[(v, u)] = -cost  # Reverse edge has negative cost to 'refund' if flow is redirected