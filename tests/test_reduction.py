import pytest
from src.complexity.reduction_demo import ReductionDemo

def test_variable_gadget_creation():
    """
    Tests that the reduction correctly creates two nodes 
    (True and False) for every input variable.
    """
    demo = ReductionDemo()
    variables = ['x', 'y', 'z']
    clauses = [['x', 'y', 'z']]
    
    graph = demo.reduce_boolean_to_graph(variables, clauses)
    
    # Check that we have 2 * number of variables nodes
    assert len(graph["nodes"]) == 6
    
    # Verify specific nodes exist
    assert "x_T" in graph["nodes"]
    assert "x_F" in graph["nodes"]
    
    # Verify the edge between T and F exists (the variable gadget)
    assert ("x_T", "x_F") in graph["edges"] or ("x_F", "x_T") in graph["edges"]

def test_empty_reduction():
    """ Tests that the reduction handles empty input gracefully. """
    demo = ReductionDemo()
    graph = demo.reduce_boolean_to_graph([], [])
    assert len(graph["nodes"]) == 0
    assert len(graph["edges"]) == 0