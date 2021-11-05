from random import randint
import time
from datetime import timedelta
from single_linked_list import *


selLinkedList = SingleLinkedList()
A = [randint(0, 1000) for x in range(100)]


for x in A:
    selLinkedList.add_list_item(x)


start_time = time.monotonic()
current_node = selLinkedList.head

while current_node is not None:
    
    jump_id = 1
    jump_node = selLinkedList.head
    while jump_id < selLinkedList.list_length():
        
        
        if jump_node.next.data < jump_node.data:
            jump_node.next.data, jump_node.data = jump_node.data, jump_node.next.data
            
        jump_node = jump_node.next
        jump_id += 1
        

    current_node = current_node.next
    
    


selLinkedList.output_list()


end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
