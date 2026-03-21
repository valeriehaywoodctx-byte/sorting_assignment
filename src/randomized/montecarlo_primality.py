import random

def fermat_test(n, k=10):
    """
    Checks if n is prime using Fermat's Little Theorem.
    k is the number of trials.
    """
    if n <= 1: return False
    if n <= 3: return True
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        # pow(a, n-1, n) is (a^(n-1)) % n
        if pow(a, n - 1, n) != 1:
            return False  # Definitely composite
    return True  # Probably prime

def miller_rabin(n, k=10):
    """
    Checks if n is prime using the Miller-Rabin primality test.
    More robust than Fermat (handles Carmichael numbers).
    """
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False # Definitely composite
    return True # Probably prime