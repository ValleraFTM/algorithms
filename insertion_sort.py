from random import randint
import time
from datetime import timedelta

start_time = time.monotonic()

A = [randint(0, 1000) for x in range(1000)]

for j in range(len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key :
        A[i+1] = A[i]
        i -= 1
        A[i+1] = key

print(A)

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
