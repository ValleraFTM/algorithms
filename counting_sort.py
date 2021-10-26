from random import randint
import time
from datetime import timedelta


start_time = time.monotonic()

k = 100

A = [randint(0, k) for x in range(200000)]


def simple_counting_sort(A):
    C = [0 for i in range(0,k + 1)]
    
    for i in range(0, len(A)):
        C[A[i]] = C[A[i]] + 1
    
    b = 0
    for j in range(0, k + 1):
        for i in range(0, C[j]):
            A[b] = j
            b += 1
        
def counting_sort(A):
    C = [0 for i in range(0,k + 1)]
    
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    C[0] = C[0] - 1
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]


    B = [None for i in range(len(A))]
    
    for j in reversed(A):
        B[C[j]] = j
        C[j] = C[j] - 1

#раскоментить для запуска простой сортировки подсчётом
#simple_counting_sort(A)

counting_sort(A)



end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
