def solve_tsp(dist_matrix):
    n = len(dist_matrix)
    # dp[mask][i] stores min cost to visit 'mask' cities ending at 'i'
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)): continue
            for v in range(n):
                if not (mask & (1 << v)):
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist_matrix[u][v])

    full_mask = (1 << n) - 1
    return min(dp[full_mask][i] + dist_matrix[i][0] for i in range(1, n))