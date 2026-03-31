from src.strings.suffix_array import build_suffix_array, build_lcp_array

class PlagiarismDetector:
    def __init__(self, doc1, doc2):
        self.doc1 = doc1
        self.doc2 = doc2
        # Create the 'Super String'
        self.combined = doc1 + "#" + doc2
        self.split_point = len(doc1)

    def find_longest_common_match(self):
        """
        Uses the Suffix Array and LCP Array to find the 
        longest identical string shared between the two docs.
        """
        sa = build_suffix_array(self.combined)
        lcp = build_lcp_array(self.combined, sa)
        
        max_len = 0
        best_match = ""
        
        # Check neighboring suffixes in the Suffix Array
        for i in range(len(lcp)):
            idx1 = sa[i]
            idx2 = sa[i+1]
            
            # Check if one suffix is from Doc1 and the other is from Doc2
            # (One index must be before the '#', one must be after)
            if (idx1 < self.split_point and idx2 > self.split_point) or \
               (idx1 > self.split_point and idx2 < self.split_point):
                
                if lcp[i] > max_len:
                    max_len = lcp[i]
                    # Extract the actual matching text
                    best_match = self.combined[idx1 : idx1 + max_len]
        
        return best_match

if __name__ == "__main__":
    d1 = "The quick brown fox jumps over the lazy dog"
    d2 = "A fast brown fox jumps over a sleeping cat"
    
    detector = PlagiarismDetector(d1, d2)
    match = detector.find_longest_common_match()
    print(f"Longest common phrase: '{match}'")