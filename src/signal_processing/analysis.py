import math
from fft.fft import FFTProcessor

class SpectralAnalyzer:
    @staticmethod
    def power_spectral_density(signal, sample_rate):
        n = len(signal)
        size = 1 << (n - 1).bit_length()
        padded = signal + [0.0] * (size - n)
        freqs = FFTProcessor.fft(padded)
        
        psd = [(abs(f)**2) / size for f in freqs[:size // 2]]
        freq_bins = [(i * sample_rate) / size for i in range(size // 2)]
        return freq_bins, psd

    @staticmethod
    def find_peak_frequency(signal, sample_rate):
        # We call the PSD method above to get the data
        freq_bins, psd = SpectralAnalyzer.power_spectral_density(signal, sample_rate)
        
        max_power = -1
        peak_freq = 0
        for i in range(len(psd)):
            if psd[i] > max_power:
                max_power = psd[i]
                peak_freq = freq_bins[i] # Fixed: use freq_bins, not freqs
        return peak_freq

    @staticmethod
    def stft(signal, frame_size, hop_size, sample_rate):
        spectrogram = []
        for i in range(0, len(signal) - frame_size, hop_size):
            window = signal[i : i + frame_size]
            freqs = FFTProcessor.fft(window)
            spectrogram.append([abs(f) for f in freqs[:frame_size // 2]])
        return spectrogram