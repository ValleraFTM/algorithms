from random import randint
import time
from datetime import timedelta


start_time = time.monotonic()

A = [randint(0, 1000) for x in range(100000)]

def quick_sort(A):
    if len(A) < 2:
        return A
    else:
        pivot = A[0]
        less = [i for i in A[1:] if i <= pivot]
        greater = [i for i in A[1:] if i > pivot]
        
        return quick_sort(less) + [pivot] + quick_sort(greater)
    


quick_sort(A)

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
