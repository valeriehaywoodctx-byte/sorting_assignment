def bubble_sort(arr: list[int]) -> list[int]:
    """Sorts a list using optimized Bubble Sort. O(n^2)"""
    if not isinstance(arr, list): raise TypeError("Input must be a list")
    data = arr.copy()
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped: break
    return data

def selection_sort(arr: list[int]) -> list[int]:
    """Sorts a list using Selection Sort. O(n^2)"""
    if not isinstance(arr, list): raise TypeError("Input must be a list")
    data = arr.copy()
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def insertion_sort(arr: list[int]) -> list[int]:
    """Sorts a list using Insertion Sort. O(n^2)"""
    if not isinstance(arr, list): raise TypeError("Input must be a list")
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data