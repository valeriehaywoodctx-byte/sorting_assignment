import pytest
from src.graphs.graph import Graph
from src.graphs.dfs import dfs

def test_dfs_traversal():
    # Linear graph: A -> B -> C
    g = Graph(directed=True)
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    
    result = dfs(g, "A")
    # In a simple line, order should be A, B, C
    assert result == ["A", "B", "C"]

def test_dfs_branching():
    g = Graph(directed=True)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("C", "D")
    
    result = dfs(g, "A")
    # DFS will pick a path (like A -> C -> D) and finish it before doing B
    assert "D" in result
    assert result[0] == "A"
    