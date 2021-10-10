from random import randint
import time
from datetime import timedelta
import sys

sys.setrecursionlimit(1500)

start_time = time.monotonic()

A = [randint(-1000, 1000) for x in range(100)]

def findMaxCrossingSubarray(A, low, mid, high):
    left_sum = -float("inf")
    summ = 0
    #max_left = mid
    for i in range(mid, low - 1, -1):
        summ += A[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i
    right_sum = -float("inf")
    summ = 0
    #max_right = mid + 1
    for j in range(mid + 1, high + 1):
        summ += A[j]
        if summ > right_sum:
            right_sum = summ
            max_right = j
    return max_left, max_right, left_sum + right_sum


print('find max crossing subarray', findMaxCrossingSubarray(A, 0, len(A) // 2, len(A) - 1))

def findMaximumSubarray(A, low, high):
    if high == low:
        return(low, high, A[low])
    else:
        mid = (low + high)// 2
        left_low, left_high, left_sum  = findMaximumSubarray(A, low, mid)
        right_low, right_high, right_sum = findMaximumSubarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = findMaxCrossingSubarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

    
print('find maximum subarray', findMaximumSubarray(A, 0, len(A) - 1))

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
