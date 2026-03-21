import random

def jaccard_similarity(set1, set2):
    """ The ground truth: (Intersection / Union) """
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union > 0 else 0

def minhash_signature(data_set, num_hashes=128):
    """ Creates a signature of the set using randomized 'permutations'. """
    signature = []
    # Use a fixed seed for each hash 'i' so signatures are comparable
    for i in range(num_hashes):
        min_hash = float('inf')
        for item in data_set:
            # Simulate a random hash function for each item
            h = hash((item, i))
            if h < min_hash:
                min_hash = h
        signature.append(min_hash)
    return signature

def estimate_similarity(sig1, sig2):
    """ Estimates Jaccard Similarity by comparing two MinHash signatures. """
    matches = sum(1 for i, j in zip(sig1, sig2) if i == j)
    return matches / len(sig1)