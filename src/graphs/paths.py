class GraphAlgorithms:
    @staticmethod
    def floyd_warshall(graph):
        """
        Finds the shortest distance between all pairs of nodes.
        graph: 2D list where graph[i][j] is the weight of edge (i, j).
        Use float('inf') for no direct connection.
        """
        n = len(graph)
        dist = [list(row) for row in graph]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist