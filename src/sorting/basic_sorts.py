def bubble_sort(arr: list[int]) -> list[int]:
    """Sorts a list using optimized Bubble Sort. O(n^2)"""
    if not isinstance(arr, list): raise TypeError("Input must be a list")
    
    # REMOVE: data = arr.copy()
    
    n = len(arr) # Change 'data' to 'arr'
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]: # Change 'data' to 'arr'
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Change 'data' to 'arr'
                swapped = True
        if not swapped: break
    return arr # Change 'data' to 'arr'

def selection_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr