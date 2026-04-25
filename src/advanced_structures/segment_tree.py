class SegmentTree:
    def __init__(self, data, func=max):
        self.n = len(data)
        self.func = func
        self.tree = [0] * (2 * self.n)
        self._build(data)

    def _build(self, data):
        # Insert leaf nodes in tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, val):
        # Update leaf node
        i += self.n
        self.tree[i] = val
        # Propagate change upwards
        while i > 1:
            i //= 2
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        # Range query [l, r]
        res = None
        l += self.n
        r += self.n
        while l <= r:
            if l % 2 == 1:
                res = self.func(res, self.tree[l]) if res is not None else self.tree[l]
                l += 1
            if r % 2 == 0:
                res = self.func(res, self.tree[r]) if res is not None else self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res