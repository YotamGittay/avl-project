from avl_template import *

# Constants for random number generation
MIN_KEY = 1
MAX_KEY = 50

NODES = [i for i in range(20)]

tree = AVLTree()
for i in range(len(NODES)):
    tree.insert(NODES[i], "")
print("*******")
for x in NODES[10:15]:
    node = tree.search(NODES[i])
    tree.delete(node)
tree.print_tree()
