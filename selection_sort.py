from random import randint
import time
from datetime import timedelta

start_time = time.monotonic()

A = [randint(0, 1000) for x in range(10000)]

for i in range(0, len(A) - 1):
    smallest = i
    for j in range(i + 1, len(A)-1):
        if A[j] < A[smallest]:
            smallest = j
    A[i], A[smallest] = A[smallest], A[i]


end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
