import pytest
from src.space_optimized_knapsack import space_optimized_knapsack

def test_knapsack_correctness():
    # Standard test case
    weights = [1, 2, 3]
    values = [6, 10, 12]
    capacity = 5
    # Result should be 22 (items with weights 2 and 3)
    result, _ = space_optimized_knapsack(weights, values, capacity)
    assert result == 22

def test_knapsack_empty():
    result, _ = space_optimized_knapsack([], [], 10)
    assert result == 0

def test_knapsack_small_capacity():
    weights = [10, 20]
    values = [100, 200]
    capacity = 5
    result, _ = space_optimized_knapsack(weights, values, capacity)
    assert result == 0