from avl_template import *

MIN_KEY = 1
MAX_KEY = 50

NODES_1 = [30,31,32,33,34,35]
NODES_2 = [24,25,26]

tree1 = AVLTree()
for i in range(len(NODES_1)):
    tree1.insert(NODES_1[i], "")
tree2 = AVLTree()
for i in range(len(NODES_2)):
    tree2.insert(NODES_2[i], "")
tree1.join(tree2, 29, "")
#
# NODES_1 = [31,30,32]
# NODES_2 = [34,35]

# tree1 = AVLTree()
# for i in range(len(NODES_1)):
#     tree1.insert(NODES_1[i], "")
# tree2 = AVLTree()
# for i in range(len(NODES_2)):
#     tree2.insert(NODES_2[i], "")
# tree1.join(tree2, 33, "")
#
# tree1.print_tree()

node = tree1.search(29)
# print("**************")
#
tree1.print_tree()
print("**************")

split2 = tree1.split2(node)
print("**************")
split2[0].print_tree()
print("**************")
split2[1].print_tree()
