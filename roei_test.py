

from avl_template import *
tree = AVLTree()

# Constants for random number generation
MIN_KEY = 1
MAX_KEY = 1000
NODES= [5,3,8,9,1,6]

# Generate and insert 50 random nodes
for i in range(len(NODES)):
    key = NODES[i]
    tree.insert(key, "")
    tree.print_tree()


node = tree.search(8)
tree.delete(node)
tree.print_tree()
