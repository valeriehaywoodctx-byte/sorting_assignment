def vertex_cover_approx(edges):
    """
    A 2-approximation greedy algorithm for Vertex Cover.
    Pick an edge, add both endpoints to the cover, and remove all connected edges.
    """
    cover = set()
    # Copy edges into a list so we can modify it
    remaining_edges = list(edges)
    
    while remaining_edges:
        # Pick the first available edge
        u, v = remaining_edges[0]
        cover.add(u)
        cover.add(v)
        
        # Remove every edge that is now 'covered' by u or v
        remaining_edges = [e for e in remaining_edges if e[0] != u and e[0] != v and e[1] != u and e[1] != v]
            
    return cover

if __name__ == "__main__":
    # Test Graph Edges
    graph_edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 2)]
    result = vertex_cover_approx(graph_edges)
    print(f"Approximated Vertex Cover: {result}")