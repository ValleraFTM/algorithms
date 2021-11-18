from random import randint
import time
from datetime import timedelta

class Tree_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Binary_tree_search:
    def __init__(self):
        self.root = None
        self.leaf = None
        

    def add_node(self, node):
        
        if not isinstance(node, Tree_node):
            is_node = Tree_node(node)
            print('node completed')
        else:
            is_node = node        
        
        if self.root is None:
            self.root = is_node
            print('root completed')
            
        else:
            current_node = self.root
            while current_node:
                              
                if current_node.value >= is_node.value:
                    if current_node.left:
                        current_node = current_node.left
                        print('move to the right')
                    else:
                        current_node.left = is_node
                        print(is_node.value, 'left')
                        return
                else:
                    if current_node.right:
                        current_node = current_node.right
                        print('move to the right')
                        
                    else:
                        current_node.right = is_node
                        print(is_node.value, 'right')
                        return
            
    def print_tree(self):
        print(root.value)

def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)
                

    
start_time = time.monotonic()

A = [randint(0, 1000) for x in range(10)]
tree = Binary_tree_search()
print(A)

for x in A:
    tree.add_node(x)

pre_order(tree.root)

