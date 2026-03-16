import pytest
from src.floyd_warshall import floyd_warshall

def test_floyd_warshall_logic():
    INF = float('inf')
    graph = [[0, 3, INF], [INF, 0, 1], [INF, INF, 0]]
    result = floyd_warshall(3, graph)
    # Shortest path from 0 to 2 should be 4 (0->1->2)
    assert result[0][2] == 4