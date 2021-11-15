
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)

def in_order(node):
    if node:
        post_order(node.left)
        print(node.value)
        post_order(node.right)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

pre_order(tree)
print()
print()
post_order(tree)
print()
print()
in_order(tree)

        
        
