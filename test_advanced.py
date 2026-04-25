import sys
import os

# 1. Setup the path
base_path = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(base_path, 'src')
sys.path.append(src_path)

# 2. Clean Imports
from advanced_structures.segment_tree import SegmentTree
from advanced_structures.fenwick_tree import FenwickTree
from advanced_structures.persistent_tree import PersistentSegmentTree
from advanced_structures.bit_vector import BitVector
from advanced_structures.wavelet_tree import WaveletTree

def test_all():
    print("--- 🌳 Testing Segment Tree ---")
    st = SegmentTree([1, 5, 2, 8], func=max)
    res = st.query(0, 2)
    print(f"Result (Max of 1, 5, 2): {res} {'✅' if res == 5 else '❌'}")

    print("\n--- 🌳 Testing Fenwick Tree ---")
    ft = FenwickTree([1, 2, 3, 4])
    res_ft = ft.range_query(0, 2)
    print(f"Result (Sum of 1, 2, 3): {res_ft} {'✅' if res_ft == 6 else '❌'}")

    print("\n--- ⏳ Testing Persistent Tree ---")
    pst = PersistentSegmentTree([1, 2, 3, 4])
    v1 = pst.update(0, 1, 10)
    v0_res = pst.query(0, 0, 3)
    v1_res = pst.query(v1, 0, 3)
    print(f"V0 Sum: {v0_res} {'✅' if v0_res == 10 else '❌'}")
    print(f"V1 Sum: {v1_res} {'✅' if v1_res == 18 else '❌'}")

    print("\n--- 🧬 Testing Succinct Bit Vector ---")
    bv = BitVector(10)
    bv.set_bit(1); bv.set_bit(3); bv.set_bit(7)
    r = bv.rank1(7)
    s = bv.select1(2)
    print(f"Rank1(7): {r} {'✅' if r == 3 else '❌'}")
    print(f"Select1(2): {s} {'✅' if s == 3 else '❌'}")

    print("\n--- 🌊 Testing Wavelet Tree (Alphabet Search) ---")
    # Sequence: ACGA (1, 2, 3, 1)
    wt = WaveletTree([1, 2, 3, 1], 1, 4)
    count_a = wt.count_occurrences(0, 3, 1)
    print(f"Count of '1' in [0, 3]: {count_a} {'✅' if count_a == 2 else '❌'}")

if __name__ == "__main__":
    test_all()