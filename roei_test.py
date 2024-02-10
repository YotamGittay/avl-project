print("****")

from avl_template import *

# Constants for random number generation
MIN_KEY = 1
MAX_KEY = 50

NODES= [i for i in range(40)]

# Generate and insert 50 random nodes


for i in range(2000):
    tree = AVLTree()
    keys = [random.randint(MIN_KEY, MAX_KEY) for j in range(13)]
    for key in keys:
        tree.insert(key, "")
    if not tree.is_avl():
        print(keys)
    
print("done! All good!")

