class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.start_index = -1

class SuffixTree:
    def __init__(self, text):
        self.root = SuffixTreeNode()
        self.text = text + "$"  # Terminal character to handle suffixes that are prefixes
        self.build_tree()

    def insert_suffix(self, suffix, original_index):
        current = self.root
        for char in suffix:
            if char not in current.children:
                current.children[char] = SuffixTreeNode()
            current = current.children[char]
        current.is_end = True
        current.start_index = original_index

    def build_tree(self):
        for i in range(len(self.text)):
            self.insert_suffix(self.text[i:], i)

    def search(self, pattern):
        """Returns True if the pattern exists anywhere in the text."""
        current = self.root
        for char in pattern:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def find_all_occurrences(self, pattern):
        """Advanced: Finds every index where the pattern appears."""
        current = self.root
        for char in pattern:
            if char not in current.children:
                return []
            current = current.children[char]
        
        # Traverse from this node to find all leaf nodes
        indices = []
        self._collect_indices(current, indices)
        return indices

    def _collect_indices(self, node, indices):
        if node.start_index != -1:
            indices.append(node.start_index)
        for child in node.children.values():
            self._collect_indices(child, indices)

if __name__ == "__main__":
    st = SuffixTree("banana")
    print(f"Suffix Tree contains 'ana'?: {st.search('ana')}")
    print(f"Suffix Tree contains 'xyz'?: {st.search('xyz')}")