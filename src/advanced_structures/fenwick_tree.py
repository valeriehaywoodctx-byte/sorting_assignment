class FenwickTree:
    def __init__(self, data):
        """
        Initializes the Fenwick Tree (Binary Indexed Tree).
        Space Complexity: O(n)
        """
        self.n = len(data)
        self.tree = [0] * (self.n + 1)
        for i, val in enumerate(data):
            self.update(i, val)

    def update(self, i, delta):
        """Adds delta to the element at index i. Complexity: O(log n)"""
        i += 1  # Fenwick trees are 1-indexed internally
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # The magic bit manipulation to find the next node

    def query(self, i):
        """Returns the prefix sum from index 0 to i. Complexity: O(log n)"""
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)  # The magic bit manipulation to find the parent node
        return s

    def range_query(self, l, r):
        """Returns the sum in the range [l, r] using prefix differences."""
        return self.query(r) - self.query(l - 1)