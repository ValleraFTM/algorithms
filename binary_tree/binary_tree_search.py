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
    def adding_node(self, node, root):
            current_node = root
            while current_node:
                if current_node.value <= node.value:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = node
                        return
                else:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = node
                    
    
    def add_node(self, node):
        
        if not isinstance(node, Tree_node):
            node = Tree_node(node)        
        if self.root is None:
            self.root = node
            
        else:
            adding_node(node, self.root)
                
            
        self.leaf = node

    
start_time = time.monotonic()

A = [randint(0, 1000) for x in range(20)]
tree = Binary_tree_search()

for x in A:
    tree.add_node(x)

    

