import random

def insertion_sort(arr: list) -> list:
    """Helper for small subarrays (Threshold optimization)."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr: list) -> list:
    """
    Optimized QuickSort: Randomized pivot + Insertion Sort threshold.
    """
    # Requirement: Do not modify original input
    data = arr[:]
    return _quicksort_recursive(data)

def _quicksort_recursive(arr: list) -> list:
    # Base Case
    if len(arr) <= 1:
        return arr

    # Optimization: Switch to Insertion Sort for small subarrays (~10)
    if len(arr) < 10:
        return insertion_sort(arr)

    # Requirement: Randomized pivot selection
    pivot = random.choice(arr)

    # Partitioning
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return _quicksort_recursive(left) + middle + _quicksort_recursive(right)