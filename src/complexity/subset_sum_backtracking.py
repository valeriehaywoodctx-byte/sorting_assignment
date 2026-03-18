import time

def subset_sum_backtracking(numbers, target, index=0, current_sum=0):
    """
    Exhaustive search using backtracking to find if a subset equals target.
    Complexity: O(2^n)
    """
    # Base Case: Found the target
    if current_sum == target:
        return True
    
    # Base Case: Reached end of list or exceeded target
    if index >= len(numbers):
        return False

    # Recursive Step 1: Include numbers[index]
    if subset_sum_backtracking(numbers, target, index + 1, current_sum + numbers[index]):
        return True

    # Recursive Step 2: Exclude numbers[index]
    if subset_sum_backtracking(numbers, target, index + 1, current_sum):
        return True

    return False

if __name__ == "__main__":
    # Small test
    data = [3, 34, 4, 12, 5, 2]
    target_val = 9
    start = time.time()
    found = subset_sum_backtracking(data, target_val)
    elapsed = time.time() - start
    print(f"Target {target_val} found? {found} (Time: {elapsed:.6f}s)")