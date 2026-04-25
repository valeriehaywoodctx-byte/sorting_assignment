class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class PersistentSegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.roots = [self._build(data, 0, self.n - 1)]

    def _build(self, data, start, end):
        if start == end:
            return Node(data[start])
        mid = (start + end) // 2
        l_child = self._build(data, start, mid)
        r_child = self._build(data, mid + 1, end)
        return Node(l_child.value + r_child.value, l_child, r_child)

    def update(self, version_idx, idx, val):
        # Creates a new root for the new version
        new_root = self._update(self.roots[version_idx], 0, self.n - 1, idx, val)
        self.roots.append(new_root)
        return len(self.roots) - 1

    def _update(self, old_node, start, end, idx, val):
        if start == end:
            return Node(val)
        mid = (start + end) // 2
        if idx <= mid:
            # New left child, reuse old right child
            new_left = self._update(old_node.left, start, mid, idx, val)
            return Node(new_left.value + old_node.right.value, new_left, old_node.right)
        else:
            # New right child, reuse old left child
            new_right = self._update(old_node.right, mid + 1, end, idx, val)
            return Node(old_node.left.value + new_right.value, old_node.left, new_right)

    def query(self, version_idx, l, r):
        return self._query(self.roots[version_idx], 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l: return 0
        if l <= start and end <= r: return node.value
        mid = (start + end) // 2
        return self._query(node.left, start, mid, l, r) + self._query(node.right, mid + 1, end, l, r)