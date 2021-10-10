from random import randint
import time
from datetime import timedelta

start_time = time.monotonic()

A = [randint(0, 1000) for x in range(1000)]

for j in range(0, len(A) - 1):
    F = 0
    for i in range(len(A) - 1 - j):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            F = 1
    if F == 0:
        break


end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
