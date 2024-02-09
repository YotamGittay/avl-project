

from avl_template import *
tree = AVLTree()

# Constants for random number generation
MIN_KEY = 1
MAX_KEY = 1000
NODES= [5,2,6,8]

# Generate and insert 50 random nodes
for i in range(len(NODES)):
    key = NODES[i]
    tree.insert(key, "")
    tree.print_tree()



