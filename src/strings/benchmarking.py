import time
from src.strings.search_engine import UnifiedSearchEngine

def run_benchmark():
    # 1. Setup data: A small text and a much larger repeated text
    small_text = "abracadabra" * 10
    large_text = "the quick brown fox jumps over the lazy dog" * 1000
    pattern = "lazy"

    engine_small = UnifiedSearchEngine(small_text)
    engine_large = UnifiedSearchEngine(large_text)
    
    methods = ['kmp', 'rabin_karp', 'suffix_tree']
    
    print(f"\n{'Method':<15} | {'Small Text (s)':<15} | {'Large Text (s)':<15}")
    print("-" * 50)

    for method in methods:
        # Time small text
        start = time.perf_counter()
        engine_small.search(pattern, method=method)
        t_small = time.perf_counter() - start

        # Time large text
        start = time.perf_counter()
        engine_large.search(pattern, method=method)
        t_large = time.perf_counter() - start

        print(f"{method:<15} | {t_small:<15.6f} | {t_large:<15.6f}")

if __name__ == "__main__":
    run_benchmark()