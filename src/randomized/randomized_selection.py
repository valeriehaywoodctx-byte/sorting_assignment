import random

def randomized_partition(arr, low, high):
    """ Reusing the same random pivot logic from QuickSort. """
    rand_pivot = random.randint(low, high)
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
    
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_select(arr, low, high, k):
    """
    Finds the kth smallest element (0-indexed).
    If k=0, finds the minimum. If k=len/2, finds the median.
    """
    if low == high:
        return arr[low]

    # Partition the array around a random pivot
    pi = randomized_partition(arr, low, high)

    # The number of elements in the left partition
    count = pi - low

    if k == count:
        return arr[pi]
    elif k < count:
        return randomized_select(arr, low, pi - 1, k)
    else:
        # Look in the right side, adjusting k for the elements skipped
        return randomized_select(arr, pi + 1, high, k - count - 1)