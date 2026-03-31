def rabin_karp_search(text, pattern, prime=1000000007, base=256):
    """
    Uses a Rolling Hash to find matches.
    'prime' handles the margin of error (collisions).
    'base' is usually 256 for ASCII characters.
    """
    n, m = len(text), len(pattern)
    if m > n: return []

    matches = []
    h_pattern = 0
    h_text = 0
    h = 1 # The value of 'base' raised to the power of m-1

    # Pre-calculate h = pow(base, m-1) % prime
    for i in range(m - 1):
        h = (h * base) % prime

    # Step 1: Calculate initial hash of pattern and first window of text
    for i in range(m):
        h_pattern = (base * h_pattern + ord(pattern[i])) % prime
        h_text = (base * h_text + ord(text[i])) % prime

    # Step 2: Slide the window over the text
    for i in range(n - m + 1):
        # Check if the 'fingerprints' match
        if h_pattern == h_text:
            # 'Las Vegas' safety check: Verify characters to handle collisions
            if text[i:i+m] == pattern:
                matches.append(i)

        # Step 3: Calculate hash for the next window (The Rolling Part)
        if i < n - m:
            # Subtract high-order digit, add low-order digit
            h_text = (base * (h_text - ord(text[i]) * h) + ord(text[i + m])) % prime
            
            # Ensure the hash is positive
            if h_text < 0:
                h_text = h_text + prime

    return matches

# Quick Test
if __name__ == "__main__":
    txt = "GEEKS FOR GEEKS"
    pat = "GEEK"
    print(f"Rabin-Karp Match Indices: {rabin_karp_search(txt, pat)}")