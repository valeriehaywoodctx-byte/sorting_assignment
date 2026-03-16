import pytest
from src.matrix_chain_multiplication import matrix_chain_order

def test_mcm_simple():
    # Dimensions for matrices: 10x30, 30x5, 5x60
    p = [10, 30, 5, 60]
    m, s = matrix_chain_order(p)
    # Correct min multiplications should be 4500
    assert m[1][3] == 4500

def test_mcm_single_matrix():
    p = [10, 20] # Only one matrix (10x20)
    m, s = matrix_chain_order(p)
    assert m[1][1] == 0