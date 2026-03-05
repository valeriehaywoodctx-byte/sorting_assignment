def merge_sort(arr: list) -> list:
    """
    Main Merge Sort function. 
    Instructions say: Do not modify original input.
    """
    # 1. Base Case: If the list has 0 or 1 items, it is already sorted.
    # Return it as a new list.
    if len(arr) <= 1:
        return arr[:]

    # 2. The "Divide": Find the middle and split the list into two halves.
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # Recursive call
    right_half = merge_sort(arr[mid:])  # Recursive call

    # 3. The "Conquer": Use the helper function to zip them back together.
    return merge(left_half, right_half)

def merge(left: list, right: list) -> list:
    """
    Helper function to merge two sorted lists into one.
    """
    result = []
    i = 0  # Pointer for the left list
    j = 0  # Pointer for the right list

    # 4. While both lists have items, compare the 'heads' and pick the smaller one.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 5. Cleanup: If items are left over in either list, add them to result.
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# This must have NO spaces before it!
if __name__ == "__main__":
    test_list = [5, 2, 9, 1, 5, 6]
    print(f"Original: {test_list}")
    print(f"Sorted:   {merge_sort(test_list)}")