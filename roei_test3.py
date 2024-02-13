from avl_template import *

MIN_KEY = 1
MAX_KEY = 50

NODES_1 = [30,31,32,33,34,35,36,37,38,39,40,41,44,50,60,66,77,88]
NODES_2 = [24,25,26,12,11,22]

tree1 = AVLTree()
for i in range(len(NODES_1)):
    tree1.insert(NODES_1[i], "")
tree2 = AVLTree()
for i in range(len(NODES_2)):
    tree2.insert(NODES_2[i], "")

tree1.print_tree()
print("*******")
tree2.print_tree()
print("*******")
print(tree1.join(tree2, 29, ""))

tree1.print_tree()