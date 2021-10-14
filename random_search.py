from random import randint
import time
from datetime import timedelta

start_time = time.monotonic()

A = [randint(0, 1000) for x in range(1000)]
x = randint(0, 1000)
B = {}

while True:
    i = randint(0, len(A) - 1)
    if x == A[i]:
        print("Find N", i)
        break
    if i not in B:
        B[i] = A[i]
    if len(B) == len(A):
        print("Not found")
        break
    
    
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
