import pytest
from src.sorting.heap import MinHeap, PriorityQueue

def test_min_heap_insertion():
    h = MinHeap()
    values = [15, 10, 20, 5, 3]
    for v in values:
        h.insert(v)
    assert h.peek() == 3  # The smallest should be at the top

def test_min_heap_extraction():
    h = MinHeap()
    values = [15, 10, 20, 5, 3]
    for v in values:
        h.insert(v)
    
    extracted = []
    while not h.is_empty():
        extracted.append(h.extract_min())
    
    # Extraction from a Min-Heap must be in ascending order
    assert extracted == [3, 5, 10, 15, 20]

def test_priority_queue():
    pq = PriorityQueue()
    pq.enqueue(100)
    pq.enqueue(10)
    pq.enqueue(50)
    assert pq.dequeue() == 10
    assert pq.dequeue() == 50
    assert pq.dequeue() == 100