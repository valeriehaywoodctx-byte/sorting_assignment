from src.sorting.quick_sort import quick_sort

def test_quick_sort_basic():
    """Checks a standard random list."""
    assert quick_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

def test_quick_sort_duplicates():
    """Requirement check: Handles many duplicates."""
    assert quick_sort([1, 2, 1, 2, 1, 2]) == [1, 1, 1, 2, 2, 2]

def test_quick_sort_sorted():
    """Requirement check: Handles already sorted data (Pivot check)."""
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quick_sort_empty():
    """Requirement check: Handles edge cases."""
    assert quick_sort([]) == []