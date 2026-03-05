from src.sorting.merge_sort import merge_sort

def test_merge_sort_basic():
    # This checks if it can sort a small list
    assert merge_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

def test_merge_sort_empty():
    # This checks the edge case of an empty list
    assert merge_sort([]) == []

def test_merge_sort_already_sorted():
    # This checks if it handles already sorted data
    assert merge_sort([1, 2, 3]) == [1, 2, 3]