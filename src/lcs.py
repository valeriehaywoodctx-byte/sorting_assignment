import time

class LCS:
    def __init__(self):
        self.memo = {}

    def top_down(self, X, Y, m, n):
        """Top-Down DP (Memoization): O(m * n)"""
        state = (m, n)
        if m == 0 or n == 0:
            return 0
        if state in self.memo:
            return self.memo[state]
        
        if X[m-1] == Y[n-1]:
            result = 1 + self.top_down(X, Y, m-1, n-1)
        else:
            result = max(self.top_down(X, Y, m, n-1), self.top_down(X, Y, m-1, n))
        
        self.memo[state] = result
        return result

    def bottom_up(self, X, Y):
        """Bottom-Up DP (Tabulation): O(m * n)"""
        m, n = len(X), len(Y)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i-1] == Y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

def run_lcs_demo():
    s1 = "DYNAMIC"
    s2 = "PROGRAMMING"
    lcs_obj = LCS()
    
    print(f"--- LCS Test ---")
    print(f"String 1: {s1}")
    print(f"String 2: {s2}")
    
    val_bu = lcs_obj.bottom_up(s1, s2)
    print(f"LCS Length (Bottom-Up): {val_bu}")

if __name__ == "__main__":
    run_lcs_demo()