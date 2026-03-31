def compute_lps(pattern):
    """
    Builds the 'Failure Function' table.
    It tells us: 'If we fail at index i, where is the next best 
    place to start matching without re-checking what we already saw?'
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # This is the 'Skip' logic
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Searches for pattern in text using the LPS table.
    Time Complexity: O(n + m)
    """
    n, m = len(text), len(pattern)
    if m == 0: return []
    
    lps = compute_lps(pattern)
    matches = []
    i = 0  # index for text
    j = 0  # index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            # Found a match! Store the starting index
            matches.append(i - j)
            j = lps[j - 1] # Look for the next potential match

        elif i < n and pattern[j] != text[i]:
            # Mismatch after j matches
            if j != 0:
                # Don't reset to 0; use the LPS table to jump
                j = lps[j - 1]
            else:
                i += 1
    return matches

# Quick Test
if __name__ == "__main__":
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    print(f"KMP Match Indices: {kmp_search(txt, pat)}")