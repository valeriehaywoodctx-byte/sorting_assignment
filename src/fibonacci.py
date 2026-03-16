import time

class Fibonacci:
    def __init__(self):
        # This dictionary stores results for Memoization (Top-Down)
        self.memo = {}

    def recursive(self, n):
        """Naive Recursive: O(2^n) - The slow way"""
        if n <= 1:
            return n
        return self.recursive(n - 1) + self.recursive(n - 2)

    def top_down(self, n):
        """Memoization: O(n) - The 'Smart' Top-Down way"""
        if n <= 1:
            return n
        if n not in self.memo:
            self.memo[n] = self.top_down(n - 1) + self.top_down(n - 2)
        return self.memo[n]

    def bottom_up(self, n):
        """Tabulation: O(n) - The 'Efficient' Bottom-Up way"""
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

def run_fib_demo():
    fib = Fibonacci()
    # We use 35 because it's large enough to show the delay in recursion
    test_val = 35
    
    print(f"\n--- Comparing Fibonacci for n={test_val} ---")
    
    # Measure Naive Recursion
    start = time.time()
    res_rec = fib.recursive(test_val)
    print(f"Naive: {res_rec} (Time: {time.time() - start:.4f}s)")
    
    # Measure Top-Down (Memoization)
    start = time.time()
    res_td = fib.top_down(test_val)
    print(f"Top-Down: {res_td} (Time: {time.time() - start:.4f}s)")
    
    # Measure Bottom-Up (Tabulation)
    start = time.time()
    res_bu = fib.bottom_up(test_val)
    print(f"Bottom-Up: {res_bu} (Time: {time.time() - start:.4f}s)\n")

if __name__ == "__main__":
    run_fib_demo()