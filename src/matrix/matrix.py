class MatrixEngine:
    @staticmethod
    def multiply(A, B):
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])
        if cols_A != rows_B:
            raise ValueError("Incompatible dimensions")
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    @staticmethod
    def power_method(A, iterations=100):
        n = len(A)
        b_k = [1.0] * n
        for _ in range(iterations):
            combined = [0.0] * n
            for i in range(n):
                for j in range(n):
                    combined[i] += A[i][j] * b_k[j]
            norm = max(abs(x) for x in combined)
            b_k = [x / (norm if norm != 0 else 1) for x in combined]
        return norm, b_k

    @staticmethod
    def lu_decomposition(A):
        """LU Decomposition with Partial Pivoting."""
        n = len(A)
        L = [[0.0] * n for _ in range(n)]
        U = [row[:] for row in A]
        P = list(range(n))

        for i in range(n):
            # Pivot
            max_row = max(range(i, n), key=lambda r: abs(U[r][i]))
            U[i], U[max_row] = U[max_row], U[i]
            P[i], P[max_row] = P[max_row], P[i]
            
            # Update L rows to match the swap in U
            for k in range(i):
                L[i][k], L[max_row][k] = L[max_row][k], L[i][k]

            L[i][i] = 1.0
            for j in range(i + 1, n):
                factor = U[j][i] / U[i][i]
                L[j][i] = factor
                for k in range(i, n):
                    U[j][k] -= factor * U[i][k]
        return P, L, U