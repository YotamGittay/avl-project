

from avl_template import *
tree = AVLTree()

# Constants for random number generation
MIN_KEY = 1
MAX_KEY = 1000
NODES= [1,2,3,4]

# Generate and insert 50 random nodes
for i in range(len(NODES)):
    key = NODES[i]
    tree.insert(key, "")
print("****")
node = tree.get_root().get_right()
tree.left_rotation(node)
tree.print_tree()
print("****")
node = tree.search(3)
tree.delete(node)
tree.print_tree()

