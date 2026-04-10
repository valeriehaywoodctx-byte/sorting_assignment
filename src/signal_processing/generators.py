import math
import random

class SignalGenerator:
    @staticmethod
    def sine_wave(freq, duration, sample_rate=44100):
        n_samples = int(duration * sample_rate)
        return [math.sin(2 * math.pi * freq * i / sample_rate) for i in range(n_samples)]

    @staticmethod
    def multi_tone(freqs, duration, sample_rate=44100):
        """Combines multiple frequencies into one signal."""
        n_samples = int(duration * sample_rate)
        signal = [0.0] * n_samples
        for f in freqs:
            for i in range(n_samples):
                signal[i] += math.sin(2 * math.pi * f * i / sample_rate)
        # Normalize to prevent clipping
        return [s / len(freqs) for s in signal]

    @staticmethod
    def chirp(start_freq, end_freq, duration, sample_rate=44100):
        """A frequency sweep from start to end."""
        n_samples = int(duration * sample_rate)
        signal = []
        for i in range(n_samples):
            t = i / sample_rate
            # Phase is the integral of frequency
            phase = 2 * math.pi * (start_freq * t + (end_freq - start_freq) * t**2 / (2 * duration))
            signal.append(math.sin(phase))
        return signal

    @staticmethod
    def white_noise(duration, sample_rate=44100):
        n_samples = int(duration * sample_rate)
        return [random.uniform(-1, 1) for _ in range(n_samples)]

    @staticmethod
    def pink_noise(duration, sample_rate=44100):
        """Pink noise has equal energy per octave (1/f power spectrum)."""
        # Simple Voss-McCartney algorithm approximation
        white = SignalGenerator.white_noise(duration, sample_rate)
        n = len(white)
        # We use a simple filter to make white noise 'pinker' (3dB/octave drop)
        pink = [0.0] * n
        b0, b1, b2 = 0, 0, 0
        for i in range(n):
            white_val = white[i]
            b0 = 0.99765 * b0 + white_val * 0.0990460
            b1 = 0.96300 * b1 + white_val * 0.2965164
            b2 = 0.57000 * b2 + white_val * 1.0526913
            pink[i] = b0 + b1 + b2 + white_val * 0.1848
        return pink