import pytest
from src.graphs.graph import Graph

def test_adjacency_list_neighbors():
    g = Graph(directed=False, use_matrix=False)
    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 10)
    
    neighbors = g.get_neighbors("A")
    assert neighbors["B"] == 5
    assert neighbors["C"] == 10
    assert len(neighbors) == 2

def test_adjacency_matrix_neighbors():
    g = Graph(directed=False, use_matrix=True)
    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 10)
    
    neighbors = g.get_neighbors("A")
    assert neighbors["B"] == 5
    assert neighbors["C"] == 10
    assert len(neighbors) == 2