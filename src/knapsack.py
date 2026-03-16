import time

class Knapsack:
    def __init__(self):
        self.memo = {}

    def top_down(self, weights, values, capacity, n):
        """Top-Down DP (Memoization): O(n * W)"""
        state = (n, capacity)
        if n == 0 or capacity == 0:
            return 0
        if state in self.memo:
            return self.memo[state]
        
        # If item is too heavy, skip it
        if weights[n-1] > capacity:
            result = self.top_down(weights, values, capacity, n-1)
        else:
            # Max of taking the item or leaving it
            result = max(
                values[n-1] + self.top_down(weights, values, capacity - weights[n-1], n-1),
                self.top_down(weights, values, capacity, n-1)
            )
        
        self.memo[state] = result
        return result

    def bottom_up(self, weights, values, capacity):
        """Bottom-Up DP (Tabulation): O(n * W)"""
        n = len(weights)
        # Create a 2D table: rows are items, columns are capacity
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                if weights[i-1] <= w:
                    dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        
        return dp[n][capacity], dp

def run_knapsack_demo():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    n = len(weights)
    
    ks = Knapsack()
    print(f"--- Knapsack Test (Capacity: {capacity}) ---")
    
    # Memoization
    val_td = ks.top_down(weights, values, capacity, n)
    print(f"Top-Down Max Value: {val_td}")
    
    # Tabulation
    val_bu, _ = ks.bottom_up(weights, values, capacity)
    print(f"Bottom-Up Max Value: {val_bu}")

if __name__ == "__main__":
    run_knapsack_demo()