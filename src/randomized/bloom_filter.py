import hashlib

class BloomFilter:
    def __init__(self, size=1000, hash_count=5):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        """ Generates hash positions for an item. """
        positions = []
        for i in range(self.hash_count):
            # Create a unique salt for each hash function
            hash_hex = hashlib.md5((str(item) + str(i)).encode()).hexdigest()
            positions.append(int(hash_hex, 16) % self.size)
        return positions

    def add(self, item):
        """ Sets bits at the hashed positions to 1. """
        for pos in self._hashes(item):
            self.bit_array[pos] = 1

    def check(self, item):
        """ Returns True if item might be in the set, False if definitely not. """
        for pos in self._hashes(item):
            if self.bit_array[pos] == 0:
                return False
        return True