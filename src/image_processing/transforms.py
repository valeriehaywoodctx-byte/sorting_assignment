from fft.fft import FFTProcessor

class ImageTransforms:
    @staticmethod
    def fft2d(matrix):
        """Performs a 2D Forward FFT."""
        # 1. FFT every row
        rows_fft = [FFTProcessor.fft(row) for row in matrix]
        
        # 2. Transpose the matrix (swap rows and columns)
        cols = list(zip(*rows_fft))
        
        # 3. FFT every column
        cols_fft = [FFTProcessor.fft(list(col)) for col in cols]
        
        # 4. Transpose back
        return [list(row) for row in zip(*cols_fft)]

    @staticmethod
    def ifft2d(matrix):
        """Performs a 2D Inverse FFT."""
        # 1. IFFT every row
        rows_ifft = [FFTProcessor.ifft(row) for row in matrix]
        
        # 2. Transpose
        cols = list(zip(*rows_ifft))
        
        # 3. IFFT every column
        cols_ifft = [FFTProcessor.ifft(list(col)) for col in cols]
        
        # 4. Transpose back and keep only real parts
        return [[val.real for val in row] for row in zip(*cols_ifft)]