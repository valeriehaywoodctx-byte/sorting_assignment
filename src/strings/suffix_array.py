def build_suffix_array(text):
    """
    Creates a sorted index of all suffixes in the text.
    Allows for lightning-fast substring searches.
    """
    n = len(text)
    # Create a list of (suffix, original_index)
    suffixes = [(text[i:], i) for i in range(n)]
    
    # Sort suffixes alphabetically
    suffixes.sort()
    
    # The Suffix Array is just the list of the original indices in their new order
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def build_lcp_array(text, suffix_array):
    """
    Constructs the Longest Common Prefix array.
    Tells us how many characters each sorted suffix shares with its neighbor.
    Uses Kasai's Algorithm logic for accuracy.
    """
    n = len(text)
    rank = [0] * n
    for i in range(n):
        rank[suffix_array[i]] = i

    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and text[i + h] == text[j + h]:
                h += 1
            lcp[rank[i] - 1] = h
            if h > 0:
                h -= 1
    return lcp

def suffix_search(text, pattern, suffix_array):
    """
    Searches for a pattern using Binary Search on the Suffix Array.
    This is much faster than scanning the whole text for repeated queries.
    """
    n = len(text)
    m = len(pattern)
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        suffix = text[suffix_array[mid]:suffix_array[mid] + m]
        
        if suffix == pattern:
            return True # Or return the index suffix_array[mid]
        elif suffix < pattern:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

if __name__ == "__main__":
    sample_text = "banana"
    sa = build_suffix_array(sample_text)
    lcp = build_lcp_array(sample_text, sa)
    
    print(f"Text: {sample_text}")
    print(f"Suffix Array (SA): {sa}")
    print(f"LCP Array: {lcp}")
    print(f"Found 'ana'?: {suffix_search(sample_text, 'ana', sa)}")