def space_optimized_knapsack(weights, values, capacity):
    n = len(weights)
    # 1D array instead of 2D grid
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Reverse loop is CRITICAL to avoid using the same item twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
            
    return dp[capacity]

def standard_knapsack_for_comparison(weights, values, capacity):
    n = len(weights)
    # The "heavy" 2D grid
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
