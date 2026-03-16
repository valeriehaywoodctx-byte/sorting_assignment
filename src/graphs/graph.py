class Graph:
    def __init__(self, directed=False, use_matrix=False):
        self.directed = directed
        self.use_matrix = use_matrix
        
        # Adjacency List: {node: {neighbor: weight}}
        self.adj_list = {}
        
        # Adjacency Matrix & Mapping
        self.adj_matrix = []
        self.nodes = [] # List of node names to track indices
        self.node_map = {} # {node_name: index}

    def add_node(self, node):
        if node not in self.node_map:
            self.node_map[node] = len(self.nodes)
            self.nodes.append(node)
            
            if self.use_matrix:
                # Add a new column to every existing row
                for row in self.adj_matrix:
                    row.append(0)
                # Add a new row of zeros
                self.adj_matrix.append([0] * len(self.nodes))
            else:
                self.adj_list[node] = {}

    def add_edge(self, u, v, weight=1):
        # Ensure both nodes exist
        if u not in self.node_map: self.add_node(u)
        if v not in self.node_map: self.add_node(v)
        
        if self.use_matrix:
            u_idx, v_idx = self.node_map[u], self.node_map[v]
            self.adj_matrix[u_idx][v_idx] = weight
            if not self.directed:
                self.adj_matrix[v_idx][u_idx] = weight
        else:
            self.adj_list[u][v] = weight
            if not self.directed:
                self.adj_list[v][u] = weight

    def get_neighbors(self, node):
        if node not in self.node_map:
            return {}
            
        if self.use_matrix:
            u_idx = self.node_map[node]
            neighbors = {}
            for v_idx, weight in enumerate(self.adj_matrix[u_idx]):
                if weight != 0:
                    neighbors[self.nodes[v_idx]] = weight
            return neighbors
        else:
            return self.adj_list.get(node, {})

    def __str__(self):
        if self.use_matrix:
            header = "    " + "  ".join(map(str, self.nodes))
            rows = []
            for i, row in enumerate(self.adj_matrix):
                rows.append(f"{self.nodes[i]}: {row}")
            return header + "\n" + "\n".join(rows)
        else:
            return str(self.adj_list)