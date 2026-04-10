import math
from fft.fft import FFTProcessor

class FFTFilters:
    @staticmethod
    def _apply_fft_filter(signal, sample_rate, filter_func):
        """Internal helper to handle the FFT/IFFT boilerplate."""
        n = len(signal)
        size = 1 << (n - 1).bit_length()
        padded = signal + [0.0] * (size - n)
        
        freqs = FFTProcessor.fft(padded)
        
        # Apply the specific filter logic (Low, High, or Band)
        for i in range(size // 2 + 1):
            # Calculate actual frequency for this index
            f = i * sample_rate / size
            multiplier = filter_func(f)
            
            freqs[i] *= multiplier
            if i > 0 and i < size // 2:
                freqs[size - i] *= multiplier
                
        filtered = FFTProcessor.ifft(freqs)
        return [val.real for val in filtered[:n]]

    @staticmethod
    def low_pass(signal, cutoff, sample_rate):
        return FFTFilters._apply_fft_filter(signal, sample_rate, lambda f: 1.0 if f <= cutoff else 0.0)

    @staticmethod
    def high_pass(signal, cutoff, sample_rate):
        return FFTFilters._apply_fft_filter(signal, sample_rate, lambda f: 1.0 if f >= cutoff else 0.0)

    @staticmethod
    def band_pass(signal, low_cutoff, high_cutoff, sample_rate):
        return FFTFilters._apply_fft_filter(signal, sample_rate, lambda f: 1.0 if low_cutoff <= f <= high_cutoff else 0.0)

    # --- Window Functions ---
    @staticmethod
    def hanning_window(n):
        return [0.5 * (1 - math.cos(2 * math.pi * i / (n - 1))) for i in range(n)]

    @staticmethod
    def hamming_window(n):
        return [0.54 - 0.46 * math.cos(2 * math.pi * i / (n - 1)) for i in range(n)]

    @staticmethod
    def blackman_window(n):
        return [0.42 - 0.5 * math.cos(2 * math.pi * i / (n - 1)) + 0.08 * math.cos(4 * math.pi * i / (n - 1)) for i in range(n)]