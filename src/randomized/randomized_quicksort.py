import random

def partition(arr, low, high):
    """ Standard partition logic using the last element as pivot. """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    """ Picks a random pivot and swaps it to the end before partitioning. """
    rand_pivot = random.randint(low, high)
    # Swap random pivot with the high element to use standard partition
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    """ The Las Vegas version of QuickSort. """
    if low < high:
        # Get the partition index using a random pivot
        pi = randomized_partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)
    return arr