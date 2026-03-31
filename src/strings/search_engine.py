from src.strings.kmp import kmp_search
from src.strings.rabin_karp import rabin_karp_search
from src.strings.suffix_array import build_suffix_array, suffix_search
from src.strings.suffix_tree import SuffixTree

class UnifiedSearchEngine:
    def __init__(self, text):
        self.text = text
        print("Pre-processing text structures...")
        self.suffix_array = build_suffix_array(text)
        self.suffix_tree = SuffixTree(text)
        print("Engine ready.")

    def search(self, pattern, method="kmp"):
        method = method.lower()
        if method == "kmp":
            return kmp_search(self.text, pattern)
        elif method == "rabin_karp":
            return rabin_karp_search(self.text, pattern)
        elif method == "suffix_array":
            return suffix_search(self.text, pattern, self.suffix_array)
        elif method == "suffix_tree":
            return self.suffix_tree.search(pattern)
        else:
            raise ValueError(f"Unknown method: {method}")