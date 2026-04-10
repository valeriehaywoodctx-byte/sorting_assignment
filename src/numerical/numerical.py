import math

def absolute_error(exact, approx):
    return abs(exact - approx)

def relative_error(exact, approx):
    if exact == 0: return abs(approx)
    return abs(exact - approx) / abs(exact)

def matrix_norm_inf(A):
    """Infinity norm: Maximum absolute row sum"""
    return max(sum(abs(x) for x in row) for row in A)

def is_ill_conditioned(A, threshold=1e10):
    """
    Very basic check: If a determinant is near zero, 
    the matrix is hard for computers to solve accurately.
    """
    # This is a placeholder for a full Condition Number check
    # which usually requires calculating an Inverse.
    pass

import math

class StabilityUtils:
    @staticmethod
    def absolute_error(exact, approx):
        """Difference between the true value and the estimate."""
        return abs(exact - approx)

    @staticmethod
    def relative_error(exact, approx):
        """Error relative to the size of the exact value."""
        if exact == 0:
            return float('inf') if approx != 0 else 0.0
        return abs(exact - approx) / abs(exact)

    @staticmethod
    def vector_norm(v, p=2):
        """
        Calculates vector norms:
        p=1: L1 (Manhattan)
        p=2: L2 (Euclidean)
        p='inf': Infinity norm
        """
        if p == 1:
            return sum(abs(x) for x in v)
        elif p == 2:
            return math.sqrt(sum(x**2 for x in v))
        elif p == 'inf':
            return max(abs(x) for x in v)
        else:
            raise ValueError("Unsupported norm type")