print("****")

from avl_template import *

# Constants for random number generation
MIN_KEY = 1
MAX_KEY = 50

NODES= [i for i in range(40)]

# Generate and insert 50 random nodes


'''
for i in range(2000):
    tree = AVLTree()
    keys = [random.randint(MIN_KEY, MAX_KEY) for j in range(13)]
    for key in keys:
        tree.insert(key, "")
    if not tree.is_avl():
        print(keys)
    
print("done! All good!")
'''


nodes1 = [random.randint(0, 100) for j in range(10)]
nodes2 = [random.randint(120, 200) for k in range(10)]
tree1 = AVLTree()
tree2 = AVLTree()
for i in nodes1:
    tree1.insert(i,i)
for k in nodes2:
    tree2.insert(k,k)
tree1.print_tree()
print(tree1.avl_to_array())
print(tree1.is_avl())
print("----------------")
tree2.print_tree()
print(tree2.avl_to_array())
print(tree2.is_avl())
print("----------------")

res = tree1.join(tree2, 4,4)

res.print_tree()
print(res.avl_to_array())
print(res.is_avl())



