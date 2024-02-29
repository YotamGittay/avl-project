import random
from AVLTree import *

for i in range(10, 11):
    keys = [i for i in range(1000 * (2**i))]
    random.shuffle(keys)
    tree1 = AVLTree()
    tree2 = AVLTree()
    for k in (keys):

        tree1.insert(k, 1)
        tree2.insert(k, 1)
    
    
    random_key = random.choice(keys)
    if (tree1.avl_to_array() == tree2.avl_to_array()):
        print("tree1 == tree2")

    left, right = tree1.split(tree1.search(random_key))
    print(tree1.costs)
    print(f"{i} random average cost = {sum(tree1.costs) / len(tree1.costs)}, random max cost = {max(tree1.costs)}")
    
    max_left = tree2.root.left.get_max()
    left, right = tree2.split(max_left)
    print(tree2.costs)
    print(f"{i} max left average cost = {sum(tree2.costs) / len(tree2.costs)}, max left max cost = {max(tree2.costs)}")

    print("----------------------------------------")
    