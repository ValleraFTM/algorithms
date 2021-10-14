from random import randint
import time
from datetime import timedelta

start_time = time.monotonic()

A = [randint(0, 1000) for x in range(1000)]
x = randint(0, 1000)


for i in A:
    if x == i:
        print("Find ", i)
        break
else:
    print('Not found')
    
    
    
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
