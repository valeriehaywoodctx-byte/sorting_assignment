import pytest
from src.graphs.graph import Graph
from src.graphs.bfs import bfs

def test_bfs_traversal():
    # Create a simple graph: A -> B, A -> C, B -> D
    g = Graph(directed=False)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    
    # BFS should visit all neighbors at distance 1 before distance 2
    # Expected: A (start), then B and C (dist 1), then D (dist 2)
    result = bfs(g, "A")
    
    assert result[0] == "A"
    assert set(result[1:3]) == {"B", "C"} # B and C are level 1
    assert result[3] == "D"                # D is level 2

def test_bfs_matrix():
    # Make sure it works on the Matrix version too!
    g = Graph(directed=False, use_matrix=True)
    g.add_edge("X", "Y")
    g.add_edge("X", "Z")
    
    result = bfs(g, "X")
    assert result[0] == "X"
    assert set(result[1:]) == {"Y", "Z"}
    