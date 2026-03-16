import pytest
from src.bitmask_tsp import solve_tsp

def test_tsp_standard():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    # Optimal path: 0 -> 1 -> 3 -> 2 -> 0 = 80
    assert solve_tsp(graph) == 80