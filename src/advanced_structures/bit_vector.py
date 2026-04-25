class BitVector:
    def __init__(self, size):
        self.size = size
        # We use a large integer as a bit-array for maximum memory efficiency
        self.bits = 0 

    def set_bit(self, i):
        """Sets the bit at position i to 1."""
        if 0 <= i < self.size:
            self.bits |= (1 << i)

    def get_bit(self, i):
        """Returns the value of the bit at position i."""
        return (self.bits >> i) & 1

    def rank1(self, i):
        """Rank1(i): Count of 1s in the range [0, i]."""
        count = 0
        for j in range(i + 1):
            if self.get_bit(j):
                count += 1
        return count

    def select1(self, k):
        """Select1(k): Find the index of the k-th '1'."""
        count = 0
        for i in range(self.size):
            if self.get_bit(i):
                count += 1
                if count == k:
                    return i
        return -1