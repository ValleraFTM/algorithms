from random import randint
import time
from datetime import timedelta
from single_linked_list import *


linkedList = SingleLinkedList()
A = [randint(0, 1000) for x in range(100)]
for x in A:
    linkedList.add_list_item(x)


start_time = time.monotonic()



