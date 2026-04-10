import cmath

class FFTProcessor:
    @staticmethod
    def _bit_reverse(n, bits):
        """Reverses the bits of an integer."""
        rev = 0
        for _ in range(bits):
            rev = (rev << 1) | (n & 1)
            n >>= 1
        return rev

    @staticmethod
    def fft(x, inverse=False):
        """
        Iterative Cooley-Tukey FFT. 
        Supports both Forward and Inverse via the 'inverse' flag.
        This can handle ~1 million points (2^20).
        """
        n = len(x)
        bits = n.bit_length() - 1
        
        # 1. Bit-reversal permutation
        result = [x[FFTProcessor._bit_reverse(i, bits)] for i in range(n)]
        
        # 2. Iterative Butterfly calculations
        angle_sign = 2j if inverse else -2j
        
        length = 2
        while length <= n:
            angle = angle_sign * cmath.pi / length
            wlen = cmath.exp(angle)
            for i in range(0, n, length):
                w = 1
                for j in range(i, i + length // 2):
                    u = result[j]
                    v = result[j + length // 2] * w
                    result[j] = u + v
                    result[j + length // 2] = u - v
                    w *= wlen
            length *= 2
            
        if inverse:
            return [val / n for val in result]
        return result

    @staticmethod
    def ifft(X):
        """Convenience wrapper for Inverse FFT."""
        return FFTProcessor.fft(X, inverse=True)

    @staticmethod
    def convolve(signal, kernel):
        """Linear convolution via zero padding and FFT."""
        size = 1 << (len(signal) + len(kernel) - 1).bit_length()
        sig_pad = signal + [0] * (size - len(signal))
        ker_pad = kernel + [0] * (size - len(kernel))
        
        sig_fft = FFTProcessor.fft(sig_pad)
        ker_fft = FFTProcessor.fft(ker_pad)
        result_fft = [sig_fft[i] * ker_fft[i] for i in range(size)]
        
        return FFTProcessor.ifft(result_fft)