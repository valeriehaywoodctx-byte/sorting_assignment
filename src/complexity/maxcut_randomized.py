import random

def randomized_max_cut(nodes, edges):
    """
    Randomized 0.5-approximation. 
    Each node flips a coin to choose a side.
    """
    side_a = set()
    side_b = set()
    
    for node in nodes:
        if random.random() > 0.5:
            side_a.add(node)
        else:
            side_b.add(node)
            
    # Count edges crossing the cut
    cut_count = 0
    for u, v in edges:
        if (u in side_a and v in side_b) or (u in side_b and v in side_a):
            cut_count += 1
            
    return side_a, side_b, cut_count

if __name__ == "__main__":
    # A simple 4-node cycle (Square)
    v = [1, 2, 3, 4]
    e = [(1, 2), (2, 3), (3, 4), (4, 1)]
    
    a, b, count = randomized_max_cut(v, e)
    print(f"Side A: {a} | Side B: {b}")
    print(f"Edges Crossing the Cut: {count} (Goal: >= 2)")