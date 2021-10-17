from random import randint
import time
from datetime import timedelta


start_time = time.monotonic()

A = [randint(0, 1000) for x in range(100)]
print(A)
def sort(A):
    build_heap(A)
    for i in range(len(A)-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

def build_heap(A):
    for i in range(len(A), - 1, -1):
        heapify(A, len(A), i)

def heapify(A, heap_size, root_idx):
    largest = root_idx
    left = 2*root_idx + 1
    right = 2*root_idx + 2

    if left < heap_size and A[left] > A[largest]:
        largest = left
        
    if right < heap_size and A[right] > A[largest]:
        largest = right
        
    if largest != root_idx:
        A[root_idx], A[largest] = A[largest], A[root_idx]
        heapify(A, heap_size, largest)

sort(A)
print(A)
    
    
    
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
