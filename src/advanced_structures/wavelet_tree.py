from .bit_vector import BitVector

class WaveletTree:
    def __init__(self, data, low, high):
        self.low = low
        self.high = high
        if low > high or not data:
            self.left = None
            self.right = None
            self.bv = None
            return

        if low == high:
            self.left = None
            self.right = None
            self.bv = None
            return

        mid = (low + high) // 2
        self.bv = BitVector(len(data))
        
        left_data = []
        right_data = []
        
        for i, val in enumerate(data):
            if val <= mid:
                # 0 is the default in our BitVector, so we stay at 0 for left
                left_data.append(val)
            else:
                self.bv.set_bit(i) # 1 goes right
                right_data.append(val)
        
        self.left = WaveletTree(left_data, low, mid)
        self.right = WaveletTree(right_data, mid + 1, high)

    def count_occurrences(self, i, j, char_val):
        """Counts how many times char_val appears in range [i, j]"""
        # Base Case: We've reached the specific character's leaf
        if self.low == self.high:
            return (j - i + 1) if self.low == char_val else 0
        
        mid = (self.low + self.high) // 2
        
        # Mapping indices:
        # r_i: number of 1s before index i
        # r_j: number of 1s up to index j
        r_i = self.bv.rank1(i - 1) if i > 0 else 0
        r_j = self.bv.rank1(j)
        
        # l_i/l_j: number of 0s (calculated by subtracting 1s from total)
        l_i = i - r_i
        l_j = (j + 1) - r_j
        
        if char_val <= mid:
            # Go Left: Use the '0' mapping
            if self.left:
                return self.left.count_occurrences(l_i, l_j - 1, char_val)
            return 0
        else:
            # Go Right: Use the '1' mapping
            if self.right:
                return self.right.count_occurrences(r_i, r_j - 1, char_val)
            return 0