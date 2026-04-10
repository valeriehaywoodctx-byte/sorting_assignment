class TSPSolver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.memo = {}

    def solve(self, mask, last_node):
        """Recursive solver with bitmasking."""
        state = (mask, last_node)
        if state in self.memo:
            return self.memo[state]

        # Base case: visited all nodes, return to start (node 0)
        if mask == (1 << self.n) - 1:
            return self.matrix[last_node][0]

        res = float('inf')
        for next_node in range(self.n):
            if not (mask & (1 << next_node)): # If not visited
                new_res = self.matrix[last_node][next_node] + \
                          self.solve(mask | (1 << next_node), next_node)
                res = min(res, new_res)
        
        self.memo[state] = res
        return res