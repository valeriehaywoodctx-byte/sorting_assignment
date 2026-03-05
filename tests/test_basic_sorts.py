import pytest
from src.sorting.basic_sorts import bubble_sort, selection_sort, insertion_sort

def test_sorts_correctly():
    """Checks if all three algorithms actually sort a list of numbers."""
    test_data = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    
    # We test copies so one sort doesn't affect the other
    data_bubble = test_data.copy()
    data_select = test_data.copy()
    data_insert = test_data.copy()
    
    bubble_sort(data_bubble)
    selection_sort(data_select)
    insertion_sort(data_insert)
    
    assert data_bubble == expected, "Bubble Sort failed!"
    assert data_select == expected, "Selection Sort failed!"
    assert data_insert == expected, "Insertion Sort failed!"

def test_empty_list():
    """Checks if the algorithms handle an empty list without crashing."""
    data = []
    bubble_sort(data)
    assert data == []