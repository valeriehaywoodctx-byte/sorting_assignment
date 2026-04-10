class Optimizer:
    @staticmethod
    def knapsack(weights, values, capacity):
        """Standard 0/1 Knapsack algorithm using Dynamic Programming."""
        n = len(weights)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if weights[i-1] <= w:
                    # Choice: Take the item or leave it
                    dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
                else:
                    # Too heavy, must leave it
                    dp[i][w] = dp[i-1][w]
        
        return dp[n][capacity]