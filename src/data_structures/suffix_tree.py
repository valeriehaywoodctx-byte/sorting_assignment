class SuffixNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class SuffixTree:
    def __init__(self, text):
        self.root = SuffixNode()
        self.text = text
        for i in range(len(text)):
            self._insert(text[i:], i)

    def _insert(self, suffix, index):
        current = self.root
        for char in suffix:
            if char not in current.children:
                current.children[char] = SuffixNode()
            current = current.children[char]
        current.index = index

    @staticmethod
    def longest_common_substring(s1, s2):
        """Finds the longest string that appears in both s1 and s2."""
        matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        longest = 0
        end_pos = 0
        
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i-1] == s2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                    if matrix[i][j] > longest:
                        longest = matrix[i][j]
                        end_pos = i
        
        return s1[end_pos - longest: end_pos]