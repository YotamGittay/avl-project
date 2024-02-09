

from avl_template import *
tree = AVLTree()

# Constants for random number generation
MIN_KEY = 1
MAX_KEY = 1000
NUM_NODES = 10

# Generate and insert 50 random nodes
for i in range(NUM_NODES):
    key = i
    tree.insert(key, value)

tree._print_tree()