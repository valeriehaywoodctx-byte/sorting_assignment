import sys
import os
import math

# 1. FIX THE PATH (The most important part!)
# This finds the 'src' folder relative to where this script is sitting.
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')

if src_path not in sys.path:
    sys.path.append(src_path)

# 2. THE IMPORTS
try:
    from matrix.matrix import MatrixEngine
    from numerical.numerical import StabilityUtils
    from fft.fft import FFTProcessor
    from signal_processing.generators import SignalGenerator
    from signal_processing.filters import FFTFilters
    from signal_processing.analysis import SpectralAnalyzer
    from image_processing.transforms import ImageTransforms
    from image_processing.filters import ImageFilters
    from data_structures.suffix_tree import SuffixTree
    from algorithms.optimization import Optimizer
    from graphs.paths import GraphAlgorithms
    from graphs.optimization import TSPSolver  
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print(f"Looked in: {sys.path[-1]}") # This helps us debug if it fails

print("-" * 40)

# --- Test 1: Matrix Multiplication ---
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
try:
    res = MatrixEngine.multiply(A, B)
    print(f"✅ Test 1: Matrix Mult Success: {res}")
except Exception as e:
    print(f"❌ Test 1: Matrix Mult Failed: {e}")

# --- Test 2: Power Method (Eigenvalues) ---
M = [[2, 0], [0, 1]]
try:
    val, vec = MatrixEngine.power_method(M)
    print(f"✅ Test 2: Power Method Success: Eigenvalue is {val}")
except Exception as e:
    print(f"❌ Test 2: Power Method Failed: {e}")

# --- Test 3: LU Decomposition ---
A_lu = [[2, 1, 1], [4, 3, 3], [8, 7, 9]]
try:
    P, L, U = MatrixEngine.lu_decomposition(A_lu)
    print(f"✅ Test 3: LU Decomposition Success! Pivoting: {P}")
except Exception as e:
    print(f"❌ Test 3: LU Decomposition Failed: {e}")

# --- Test 4: Numerical Stability (Norms) ---
v_test = [3, -4] 
try:
    l2 = StabilityUtils.vector_norm(v_test, p=2)
    print(f"✅ Test 4: Norms & Stability Success: L2 Norm is {l2}")
except Exception as e:
    print(f"❌ Test 4: Stability Test Failed: {e}")

# --- Test 5: Forward FFT ---
signal_dc = [1.0, 1.0, 1.0, 1.0]
try:
    freqs = FFTProcessor.fft(signal_dc)
    print(f"✅ Test 5: FFT Success! DC Component: {freqs[0].real}")
except Exception as e:
    print(f"❌ Test 5: FFT Failed: {e}")

# --- Test 6: Inverse FFT (Recovery) ---
original = [1.0, 2.0, 3.0, 4.0]
try:
    freqs = FFTProcessor.fft(original)
    recovered = FFTProcessor.ifft(freqs)
    val = round(recovered[0].real, 1)
    print(f"✅ Test 6: IFFT Success! Recovered first value: {val}")
except Exception as e:
    print(f"❌ Test 6: IFFT Failed: {e}")

# --- Test 7: Convolution ---
sig = [1, 1, 1]
ker = [1, 1]
try:
    result = FFTProcessor.convolve(sig, ker)
    print(f"✅ Test 7: Convolution Success! Result length: {len(result)}")
except Exception as e:
    print(f"❌ Test 7: Convolution Failed: {e}")

# --- Test 8: Performance Stress Test ---
import time
large_n = 2**16 
large_signal = [1.0] * large_n
try:
    start_time = time.time()
    FFTProcessor.fft(large_signal)
    end_time = time.time()
    print(f"✅ Test 8: Performance Success! {large_n} points in {end_time - start_time:.2f}s")
except Exception as e:
    print(f"❌ Test 8: Performance Failed: {e}")

# --- Test 9: Signal Generation & Filtering ---
try:
    tone = SignalGenerator.sine_wave(440, 0.05, 8192)
    filtered = FFTFilters.low_pass(tone, 500, 8192)
    print(f"✅ Test 9: Signal Filtering Success! Output length: {len(filtered)}")
except Exception as e:
    print(f"❌ Test 9: Signal Test Failed: {e}")

print("-" * 40)
print("All Foundation Checks Complete!")

# --- Test 10: Advanced Filters & Windows ---
try:
    # Test High-pass
    tone_low = SignalGenerator.sine_wave(100, 0.05, 8192)
    filtered_hp = FFTFilters.high_pass(tone_low, 500, 8192)
    
    # Test Hamming Window
    win = FFTFilters.hamming_window(100)
    
    print(f"✅ Test 10: High-pass & Windows Success!")
    print(f"   Window max value: {max(win):.2f}")
except Exception as e:
    print(f"❌ Test 10: Advanced Signal Test Failed: {e}")

    # --- Test 11: Advanced Signal Generation ---
try:
    # Generate a chirp from 100Hz to 1000Hz
    sweep = SignalGenerator.chirp(100, 1000, 0.1, 8192)
    # Generate pink noise
    p_noise = SignalGenerator.pink_noise(0.1, 8192)
    
    print(f"✅ Test 11: Chirp & Pink Noise Success!")
    print(f"   Chirp Samples: {len(sweep)}")
except Exception as e:
    print(f"❌ Test 11: Advanced Generation Failed: {e}")

    # --- Test 12: Spectral Analysis (Peak Detection) ---
try:
    # Generate a pure 1000Hz tone
    test_freq = 1000
    sample_rate = 8192
    tone = SignalGenerator.sine_wave(test_freq, 0.2, sample_rate)
    
    # Detect it
    detected_freq = SpectralAnalyzer.find_peak_frequency(tone, sample_rate)
    
    # We allow a small margin of error due to FFT binning
    if abs(detected_freq - test_freq) < 20:
        print(f"✅ Test 12: Peak Detection Success! Detected: {detected_freq:.1f}Hz")
    else:
        print(f"❌ Test 12: Detection inaccurate. Expected 1000, got {detected_freq}")
except Exception as e:
    print(f"❌ Test 12: Spectral Analysis Failed: {e}")

  # --- Test 13: 2D Image Transforms ---
try:
    image = [
        [1.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 1.0],
        [1.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 1.0]
    ]
    
    freqs_2d = ImageTransforms.fft2d(image)
    recovered = ImageTransforms.ifft2d(freqs_2d)
    
    # Check top-left pixel (it should be 1.0)
    val = round(recovered[0][0], 2)
    if val == 1.0:
        print(f"✅ Test 13: 2D Transform Success! Recovered: {val}")
    else:
        print(f"❌ Test 13: Recovery inaccurate. Got {val}")
except Exception as e:
    print(f"❌ Test 13: 2D Transform Failed: {e}")

    # --- Test 14: Image Filtering (Blur) ---
try:
    image_5x5 = [[float(x+y) for x in range(8)] for y in range(8)] # 8x8 is power of 2
    blurred = ImageFilters.low_pass(image_5x5, radius=0.1)
    if len(blurred) == 8:
        print(f"✅ Test 14: Image Blur Success!")
except Exception as e:
    print(f"❌ Test 14: Image Blur Failed: {e}")

# --- Test 15: Image Compression ---
try:
    compressed = ImageFilters.compress(image_5x5, threshold=0.5)
    print(f"✅ Test 15: Image Compression Success!")
except Exception as e:
    print(f"❌ Test 15: Compression Failed: {e}")

    # --- Test 16: Suffix Tree / LCS ---
try:
    s1 = "ALGORITHM"
    s2 = "RHYTHM"
    lcs = SuffixTree.longest_common_substring(s1, s2)
    if lcs == "RHYTHM"[-3:]: # "THM"
        print(f"✅ Test 16: Longest Common Substring Success! Found: {lcs}")
    else:
        print(f"❌ Test 16: LCS Incorrect. Found: {lcs}")
except Exception as e:
    print(f"❌ Test 16: Suffix Tree Failed: {e}")

# --- Test 17: Knapsack Optimization ---
try:
    w = [1, 2, 3]
    v = [10, 15, 40]
    cap = 5
    max_val = Optimizer.knapsack(w, v, cap)
    if max_val == 55: # (15 + 40)
        print(f"✅ Test 17: Knapsack Success! Max Value: {max_val}")
except Exception as e:
    print(f"❌ Test 17: Knapsack Failed: {e}")

    # --- Test 18: Floyd-Warshall ---
try:
    inf = float('inf')
    test_graph = [
        [0, 3, inf, 7],
        [8, 0, 2, inf],
        [5, inf, 0, 1],
        [2, inf, inf, 0]
    ]
    distances = GraphAlgorithms.floyd_warshall(test_graph)
    if distances[0][2] == 5: # 0 -> 1 -> 2 (3 + 2)
        print(f"✅ Test 18: Floyd-Warshall Success! Dist(0,2): {distances[0][2]}")
except Exception as e:
    print(f"❌ Test 18: Floyd-Warshall Failed: {e}")

# --- Test 19: TSP Solver ---
try:
    tsp_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    solver = TSPSolver(tsp_matrix)
    min_cost = solver.solve(1, 0) # Start at node 0 with only node 0 visited
    if min_cost == 80:
        print(f"✅ Test 19: TSP Success! Optimal Route Cost: {min_cost}")
except Exception as e:
    print(f"❌ Test 19: TSP Failed: {e}")